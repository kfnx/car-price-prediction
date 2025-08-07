from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pandas as pd
from .prediction import predict_price
from .schema import CarFeaturesRaw, PredictionOut
from .preprocess import preprocess_data 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Setup Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Konfigurasi CORS
# PERINGATAN: Konfigurasi ini sangat permisif dan cocok untuk development.
# Untuk produksi, batasi origin ke domain frontend Anda.
# Contoh: origins = ["https://your-frontend-domain.com"]
origins = [
    "*" # Mengizinkan semua origin, cocok untuk development
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (misalnya untuk CSS, JS, gambar)
# Pastikan Anda memiliki folder 'static' di root proyek Anda.
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.post("/predict/", response_model=PredictionOut)
def predict(features: CarFeaturesRaw):
    """
    Endpoint untuk prediksi harga mobil.
    Sekarang menerima data mentah dan melakukan preprocessing.
    """
    # Ubah fitur mentah menjadi DataFrame
    df_raw = pd.DataFrame([features.dict()])
    
    # Lakukan preprocessing data
    df_processed = preprocess_data(df_raw)
    
    # Lakukan prediksi dengan data yang sudah diproses
    price = predict_price(df_processed)
    
    return {"price": price}

@app.get("/api")
def api_root():
    return {"message": "Selamat datang di API Prediksi Harga Mobil"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "car-prediction-api"}

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/faq/", response_class=HTMLResponse)
def read_faq(request: Request):
    return templates.TemplateResponse("faq.html", {"request": request})
