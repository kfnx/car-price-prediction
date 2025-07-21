import joblib
import pandas as pd
import numpy as np

# Muat model dan scaler
model = joblib.load('model/model.pkl')
scaler = joblib.load('model/scaler.pkl')

# Dapatkan daftar fitur yang diharapkan oleh scaler
expected_features = scaler.feature_names_in_
# Temukan indeks/posisi kolom 'price'
price_column_index = list(expected_features).index('price')
# Buat daftar fitur untuk model (semua kecuali 'price')
model_features = [f for f in expected_features if f != 'price']


def predict_price(data: pd.DataFrame) -> float:
    """
    Memprediksi harga mobil berdasarkan data input yang sudah diproses.
    
    Args:
        data: DataFrame dengan data mobil yang sudah diproses.
        
    Returns:
        Harga prediksi dalam skala aslinya.
    """
    data['price'] = 0
    data_reordered = data.reindex(columns=expected_features, fill_value=0)
    data_scaled = scaler.transform(data_reordered)
    data_scaled_df = pd.DataFrame(data_scaled, columns=expected_features)
    data_for_prediction = data_scaled_df[model_features]
    prediction_scaled = model.predict(data_for_prediction)
    data_scaled[0, price_column_index] = prediction_scaled[0]
    unscaled_data = scaler.inverse_transform(data_scaled)
    final_price = unscaled_data[0, price_column_index]
    
    return final_price
