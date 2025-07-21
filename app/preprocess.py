import pandas as pd

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Pra-pemrosesan data mentah untuk prediksi harga mobil.
    """
    df = df.copy()

    # Mapping fitur kategorikal
    fueltype_map = {'diesel': 0, 'gas': 1}
    aspiration_map = {'std': 0, 'turbo': 1}
    doornumber_map = {'four': 0, 'two': 1}
    carbody_map = {'convertible': 0, 'hardtop': 1, 'hatchback': 2, 'sedan': 3, 'wagon': 4}
    drivewheel_map = {'4wd': 0, 'fwd': 1, 'rwd': 2}
    enginelocation_map = {'front': 0, 'rear': 1}
    enginetype_map = {'dohc': 0, 'dohcv': 1, 'l': 2, 'ohc': 3, 'ohcf': 4, 'ohcv': 5, 'rotor': 6}
    cylindernumber_map = {'eight': 0, 'five': 1, 'four': 2, 'six': 3, 'three': 4, 'twelve': 5, 'two': 6}
    fuelsystem_map = {'1bbl': 0, '2bbl': 1, '4bbl': 2, 'idi': 3, 'mfi': 4, 'mpfi': 5, 'spdi': 6, 'spfi': 7}
    compName_map = {
        'alfa-romero': 0, 'audi': 1, 'bmw': 2, 'buick': 3, 'chevrolet': 4, 'dodge': 5,
        'honda': 6, 'isuzu': 7, 'jaguar': 8, 'mazda': 9, 'mercury': 10, 'mitsubishi': 11,
        'nissan': 12, 'peugeot': 13, 'plymouth': 14, 'porsche': 15, 'renault': 16,
        'saab': 17, 'subaru': 18, 'toyota': 19, 'volkswagen': 20, 'volvo': 21
    }

    df['fueltype'] = df['fueltype'].map(fueltype_map)
    df['aspiration'] = df['aspiration'].map(aspiration_map)
    df['doornumber'] = df['doornumber'].map(doornumber_map)
    df['carbody'] = df['carbody'].map(carbody_map)
    df['drivewheel'] = df['drivewheel'].map(drivewheel_map)
    df['enginelocation'] = df['enginelocation'].map(enginelocation_map)
    df['enginetype'] = df['enginetype'].map(enginetype_map)
    df['cylindernumber'] = df['cylindernumber'].map(cylindernumber_map)
    df['fuelsystem'] = df['fuelsystem'].map(fuelsystem_map)
    
    # Proses 'CarName' untuk 'compName'
    if 'CarName' in df.columns:
        df['compName'] = df['CarName'].apply(lambda x: x.split(' ')[0])
        df['compName'].replace({
            'maxda': 'mazda', 'Nissan ': 'nissan', 'porcshce': 'porsche',
            'toyouta': 'toyota', 'vokswagen': 'volkswagen', 'vw': 'volkswagen',
            'Nissan': 'nissan'
        }, inplace=True)
        df['compName'] = df['compName'].map(compName_map)
        df.drop('CarName', axis=1, inplace=True)

    # Gabungkan fitur mpg
    if 'citympg' in df.columns and 'highwaympg' in df.columns:
        df['avg_mpg'] = (df['citympg'] + df['highwaympg']) / 2
        df.drop(['citympg', 'highwaympg'], axis=1, inplace=True)

    # Buat fitur baru 'size_index'
    if 'carlength' in df.columns and 'carwidth' in df.columns and 'carheight' in df.columns:
        df['size_index'] = df['carlength'] * df['carwidth'] * df['carheight']
        df.drop(['carlength', 'carwidth'], axis=1, inplace=True)

    # Hapus kolom yang tidak diperlukan
    if 'car_ID' in df.columns:
        df.drop(['car_ID'], axis=1, inplace=True)
    if 'symboling' in df.columns:
        df.drop(['symboling'], axis=1, inplace=True)

    return df
