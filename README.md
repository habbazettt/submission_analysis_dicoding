# 📊 Bike Sharing Analysis Dashboard

🚴 **Bike Sharing Analysis Dashboard** adalah aplikasi berbasis Streamlit untuk melakukan analisis eksploratif terhadap dataset *Bike Sharing* dari Kaggle. Dashboard ini menyediakan berbagai visualisasi interaktif untuk memahami pola penggunaan sepeda berdasarkan berbagai faktor seperti cuaca, musim, hari kerja, dan lainnya.

## 🔗 Live Demo

🎯 **Lihat dashboard di sini:** [Bike Sharing Analysis Dashboard](https://submissionanalysisdicoding-buegwara5actjikcjjseck.streamlit.app/)

## 📂 Dataset

Dataset yang digunakan dalam proyek ini berasal dari Kaggle:

- **day.csv** (Agregasi harian dari penyewaan sepeda)
- **hour.csv** (Agregasi per jam dari penyewaan sepeda)

## 🎯 Fitur Utama

✅ **Exploratory Data Analysis (EDA)** untuk memahami tren utama dalam penggunaan sepeda.
✅ **Visualisasi interaktif** menggunakan Plotly dan Matplotlib.
✅ **Analisis faktor-faktor utama** seperti cuaca, musim, dan hari kerja.
✅ **Analisis lanjutan** termasuk RFM Analysis dan Clustering manual.
✅ **Kesimpulan dan insight** yang jelas untuk membantu pengambilan keputusan.

## 🛠️ Instalasi & Menjalankan Aplikasi

### **1️⃣ Clone Repository**

```bash
git clone https://github.com/habbazettt/submission_analysis_dicoding
cd submission_analysis_dicoding
```

### **2️⃣ Buat Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate  # Untuk macOS/Linux
venv\Scripts\activate    # Untuk Windows
```

### **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4️⃣ Jalankan Dashboard**

```bash
streamlit run dashboard/dashboard.py
```

## 📌 Teknologi yang Digunakan

- **Python** (pandas, numpy, seaborn, matplotlib, plotly)
- **Streamlit** untuk membuat dashboard interaktif
