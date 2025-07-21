from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import pandas as pd
from .prediction import predict_price
from .schema import CarFeaturesRaw, PredictionOut
from .preprocess import preprocess_data 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Konfigurasi CORS
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

# Mount static files
app.mount("/static", StaticFiles(directory="templates"), name="static")

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

@app.get("/")
def read_root():
    return FileResponse('templates/index.html')
