# Proyek Prediksi Harga Mobil

Selamat datang di Proyek Prediksi Harga Mobil!  
Aplikasi ini menggunakan model machine learning untuk memberikan estimasi harga mobil berdasarkan fitur yang Anda masukkan. Backend dibangun dengan FastAPI, frontend menggunakan HTML sederhana.

---

## 📜 Daftar Isi

- Struktur Proyek
- Teknologi yang Digunakan
- Langkah Menjalankan Proyek
- (Opsional) Deployment dengan Docker

---

## 📁 Struktur Proyek

```
car-price-prediction/
│
├── app/                  # Folder utama aplikasi API (FastAPI)
│   ├── main.py           # Endpoint API utama dan konfigurasi
│   ├── prediction.py     # Fungsi untuk memuat model dan
│   ├── preprocess.py     # Fungsi untuk pra-pemrosesan data input
│   └── schema.py         # Skema Pydantic untuk validasi data

├── model/                # Folder berisi model yang sudah dilatih
│   ├── model.pkl         # File model machine learning
│   └── scaler.pkl        # File scaler untuk normalisasi data
│
├── data/                 # Dataset yang digunakan untuk training
│   └── CarPrice_Assignment.csv
│
├── notebooks/            # Notebook Jupyter untuk eksperimen dan
    └── car_price_model.ipynb


```

---

## 🚀 Teknologi yang Digunakan

- **Backend:** Python, FastAPI
- **Frontend:** HTML, Tailwind CSS (via CDN), JavaScript
- **Machine Learning:** Scikit-learn, Pandas
- **Server:** Uvicorn
- **Containerization:** Docker

---

## 🛠️ Langkah Menjalankan Proyek

### 1. Persiapan Lingkungan

Pastikan Anda sudah menginstal **Python 3.8+** dan **pip**.

#### a. Unduh atau Clone Proyek

Unduh semua file dan pastikan struktur folder sesuai dengan penjelasan di atas.

#### b. Buat dan Aktifkan Virtual Environment

Disarankan menggunakan virtual environment untuk mengisolasi dependensi proyek.

```sh
# Buka terminal di direktori utama proyek

# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
# - Untuk Windows:
venv\Scripts\activate

# - Untuk macOS/Linux:
source venv/bin/activate
```

#### c. Instal Dependensi

Instal semua library yang diperlukan:

```sh
pip install -r requirements.txt
```

---

### 2. Jalankan Server API (Backend)

Setelah semua library terinstal, jalankan server FastAPI:

```sh
uvicorn app.main:app --reload
```

Server akan berjalan di `http://127.0.0.1:8000`.  
Buka `http://127.0.0.1:8000/docs` di browser untuk dokumentasi interaktif (Swagger UI).

---

### 3. Gunakan Antarmuka Pengguna (Frontend)

- Pastikan server API sudah berjalan.
- Buka file `index.html` di browser Anda.
- Isi form dengan fitur mobil yang ingin diprediksi, klik "Prediksi Harga", dan estimasi harga akan muncul.

---

## (Opsional) Deployment dengan Docker

Jika Anda memiliki Docker, Anda dapat menjalankan aplikasi di dalam container.

### a. Build Docker Image

```sh
docker build -t car-prediction-api .
```

### b. Jalankan Docker Container

```sh
docker run -d --name car-api-container -p 8000:8000 car-prediction-api
```

API akan berjalan di `http://localhost:8000`.  
Frontend tetap dibuka secara lokal di browser Anda.
