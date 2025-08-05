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
├── templates/            # Frontend files  
│   └── index.html        # Web interface untuk prediksi
│   └── faq.html          # Halaman FAQ
│
├── static/               # File statis (CSS, JS, Gambar)
│   └── js/
│
├── pyproject.toml        # Project dependencies dan konfigurasi
├── requirements.txt      # Legacy dependencies file (optional)
└── .gitignore           # Files yang diabaikan git

```

---

## 🚀 Teknologi yang Digunakan

- **Package Manager:** uv (fast Python package manager)
- **Backend:** Python, FastAPI
- **Frontend (Templating):** Jinja2, HTML, Tailwind CSS (via CDN), JavaScript
- **Machine Learning:** Scikit-learn, Pandas
- **Server:** Uvicorn
- **Containerization:** Docker

---

## 🛠️ Langkah Menjalankan Proyek

### 1. Persiapan Lingkungan

Pastikan Anda sudah menginstal **Python 3.11+**.

#### a. Unduh atau Clone Proyek

Unduh semua file dan pastikan struktur folder sesuai dengan penjelasan di atas.

#### b. Instal uv

Instal uv package manager (jika belum terinstal):

```sh
# macOS/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows:
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### c. Instal Dependensi

uv akan otomatis mengelola virtual environment dan dependensi:

```sh
uv sync
```

---

### 2. Jalankan Server API (Backend)

Setelah semua library terinstal, jalankan server FastAPI dengan uv:

```sh
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Server akan berjalan di `http://localhost:8000`.

---

### 3. Akses Aplikasi

- **Frontend (UI Form):** Buka `http://localhost:8000` di browser Anda
- **API Documentation:** Buka `http://localhost:8000/docs` untuk dokumentasi interaktif (Swagger UI)
- **API Info:** Buka `http://localhost:8000/api` untuk pesan selamat datang API

Isi form dengan fitur mobil yang ingin diprediksi, klik "Prediksi Harga", dan estimasi harga akan muncul.

---

## 📦 Manajemen Dependensi dengan uv

Proyek ini menggunakan **uv** sebagai package manager yang lebih cepat daripada pip tradisional.

### Keuntungan uv:
- ✅ Manajemen virtual environment otomatis
- ✅ Instalasi dependensi yang sangat cepat  
- ✅ Lockfile untuk reproducible builds
- ✅ Tidak perlu aktivasi manual environment

### Perintah uv yang berguna:

```sh
# Menjalankan aplikasi
uv run uvicorn app.main:app --reload

# Menambah dependensi baru
uv add pandas numpy

# Menambah development dependencies  
uv add --dev pytest

# Update semua dependensi
uv sync --upgrade

# Menjalankan skrip Python apa pun
uv run python script.py
```

---

## 🐳 Deployment dengan Docker

Proyek ini telah dikonfigurasi untuk menjalankan dengan Docker menggunakan uv.

### Prasyarat
- Docker terinstal di sistem Anda
- Pastikan semua file proyek (app/, model/, templates/) ada di direktori

### Langkah-langkah Docker:

#### 1. Build Docker Image
```sh
docker build -t car-prediction-api .
```

#### 2. Jalankan Container
```sh
docker run -d --name car-api-container -p 8000:8000 car-prediction-api
```

#### 3. Akses Aplikasi
- **Frontend:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs
- **API Info:** http://localhost:8000/api

### Perintah Docker Berguna:

```sh
# Lihat container yang berjalan
docker ps

# Lihat logs container
docker logs car-api-container

# Masuk ke container (debugging)
docker exec -it car-api-container /bin/bash

# Hentikan container
docker stop car-api-container

# Hapus container
docker rm car-api-container

# Hapus image
docker rmi car-prediction-api
```
