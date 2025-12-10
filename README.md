# Eksperimen dan Preprocessing Dataset – Telco Customer Churn

Repository ini dibuat untuk memenuhi **Kriteria 1 – Eksperimen & Preprocessing** pada proyek Machine Learning Operations (MLOps).  
Pada tahap ini dilakukan:

- Eksplorasi dataset  
- Preprocessing manual pada notebook  
- Pembuatan script preprocessing otomatis  
- Pembuatan workflow CI menggunakan GitHub Actions  

---

## 1. Dataset
Dataset yang digunakan: **Telco Customer Churn**  
Sumber dataset: https://www.kaggle.com/datasets/blastchar/telco-customer-churn

Struktur folder:


namadataset_raw/
└── Telco-Customer-Churn.csv


---

## 2. Eksperimen Notebook
Notebook eksperimen berisi:

- Pengenalan dataset  
- EDA (Exploratory Data Analysis)  
- Tahap preprocessing manual  
- Pengecekan hasil preprocessing  

File notebook:  
➡️ `Eksperimen_SML_DiahAyuPuspasari.ipynb`

---

## 3. Script Preprocessing Otomatis
Script otomatis dibuat untuk menyamakan proses preprocessing dengan yang dilakukan pada notebook.

File:  
➡️ `preprocessing/automate_DiahAyuPuspasari.py`

Script ini melakukan:

- Konversi tipe data  
- Penanganan missing values  
- Remove kolom yang tidak diperlukan  
- Encoding (binary & one-hot encoding)  
- Menyimpan dataset hasil preprocessing  

Cara menjalankan script:

```bash
python preprocessing/automate_DiahAyuPuspasari.py \
    --input namadataset_raw/Telco-Customer-Churn.csv \
    --output preprocessing/telco_processed_ci.csv
```

---

### 4. GitHub Actions – Workflow CI Preprocessing

Workflow otomatis mengeksekusi script preprocessing setiap terjadi:
- Commit/push ke branch main
- Manual trigger di GitHub Actions
- Lokasi workflow:
➡️ .github/workflows/preprocess.yml
- Workflow menghasilkan artifact:
➡️ processed-dataset.zip
yang berisi:
telco_processed_ci.csv

--- 

### 5. Struktur Repository
```bash
Eksperimen_SML_DiahAyuPuspasari/
├── .github/workflows/preprocess.yml
├── namadataset_raw/
│     └── Telco-Customer-Churn.csv
├── preprocessing/
│     ├── automate_DiahAyuPuspasari.py
│     ├── telco_processed_ci.csv   (artifact lokal)
├── Eksperimen_SML_DiahAyuPuspasari.ipynb
├── README.md
```

---

### 6. Hasil CI (Continuous Integration)

Workflow berhasil dijalankan dan menghasilkan:
- Status: ✔️ Success
- Artifact: processed-dataset
- Output: telco_processed_ci.csv

Screenshot hasil CI disertakan pada folder submission Dicoding.

---

### 7. Link Repository
https://github.com/Diahayuups/Eksperimen_SML_DiahAyuPuspasari
