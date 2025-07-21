from fastapi import FastAPI
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

@app.get("/")
def read_root():
    return {"message": "Selamat datang di API Prediksi Harga Mobil"}
