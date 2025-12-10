import argparse
import pandas as pd
import numpy as np

def preprocess(input_path, output_path):
    # Load dataset
    df = pd.read_csv(input_path)

    # 1. Convert TotalCharges to numeric
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # 2. Handle missing values in TotalCharges
    df.loc[df['TotalCharges'].isna(), 'TotalCharges'] = (
        df.loc[df['TotalCharges'].isna(), 'MonthlyCharges'] *
        df.loc[df['TotalCharges'].isna(), 'tenure']
    )

    # 3. Remove unnecessary columns
    df_processed = df.drop(columns=['customerID']).copy()

    # 4. Encode Yes/No binary columns (EXCLUDING Churn)
    binary_cols = [
        c for c in df_processed.columns
        if set(df_processed[c].dropna().unique()) <= set(['Yes', 'No'])
        and c != 'Churn'
    ]

    for col in binary_cols:
        df_processed[col] = df_processed[col].map({'Yes': 1, 'No': 0})

    # 5. Handle special categories ("No internet service", "No phone service")
    replace_cols = [
        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
        'TechSupport', 'StreamingTV', 'StreamingMovies',
        'MultipleLines'
    ]

    for col in replace_cols:
        if col in df_processed.columns:
            df_processed[col] = df_processed[col].replace({
                'No internet service': 'No',
                'No phone service': 'No'
            })
            # Re-encode if still Yes/No form
            if set(df_processed[col].unique()) <= set(['Yes', 'No']):
                df_processed[col] = df_processed[col].map({'Yes': 1, 'No': 0})

    # 6. One-Hot Encoding for categorical variables
    categorical_cols = df_processed.select_dtypes(include=['object']).columns.tolist()
    categorical_cols = [c for c in categorical_cols if c != 'Churn']

    df_processed = pd.get_dummies(df_processed, columns=categorical_cols, drop_first=True)

    # 7. Encode target variable Churn
    df_processed['Churn'] = df_processed['Churn'].map({'Yes': 1, 'No': 0})

    # 8. Save the processed dataset
    df_processed.to_csv(output_path, index=False)

    print(f"Preprocessing complete! Output saved to: {output_path}")
    print("Final shape:", df_processed.shape)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True, help="Path to raw CSV file")
    parser.add_argument("--output", type=str, required=True, help="Path to save processed CSV")
    args = parser.parse_args()

    preprocess(args.input, args.output)
