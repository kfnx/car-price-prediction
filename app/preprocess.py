import pandas as pd

# --- Mapping categorical Features ---

FUELTYPE_MAP = {'diesel': 0, 'gas': 1}
ASPIRATION_MAP = {'std': 0, 'turbo': 1}
DOORNUMBER_MAP = {'four': 0, 'two': 1}
CARBODY_MAP = {'convertible': 0, 'hardtop': 1, 'hatchback': 2, 'sedan': 3, 'wagon': 4}
DRIVEWHEEL_MAP = {'4wd': 0, 'fwd': 1, 'rwd': 2}
ENGINELOCATION_MAP = {'front': 0, 'rear': 1}
ENGINETYPE_MAP = {'dohc': 0, 'dohcv': 1, 'l': 2, 'ohc': 3, 'ohcf': 4, 'ohcv': 5, 'rotor': 6}
CYLINDERNUMBER_MAP = {'eight': 0, 'five': 1, 'four': 2, 'six': 3, 'three': 4, 'twelve': 5, 'two': 6}
FUELSYSTEM_MAP = {'1bbl': 0, '2bbl': 1, '4bbl': 2, 'idi': 3, 'mfi': 4, 'mpfi': 5, 'spdi': 6, 'spfi': 7}

COMP_NAME_MAP = {
    'alfa-romero': 0, 'audi': 1, 'bmw': 2, 'buick': 3, 'chevrolet': 4, 'dodge': 5,
    'honda': 6, 'isuzu': 7, 'jaguar': 8, 'mazda': 9, 'mercury': 10, 'mitsubishi': 11,
    'nissan': 12, 'peugeot': 13, 'plymouth': 14, 'porsche': 15, 'renault': 16,
    'saab': 17, 'subaru': 18, 'toyota': 19, 'volkswagen': 20, 'volvo': 21
}

CAR_NAME_CORRECTIONS = {
    'maxda': 'mazda',
    'Nissan ': 'nissan',
    'porcshce': 'porsche',
    'toyouta': 'toyota',
    'vokswagen': 'volkswagen',
    'vw': 'volkswagen',
    'Nissan': 'nissan'
}


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Pra-pemrosesan data mentah untuk prediksi harga mobil.
    """
    df = df.copy()

    # Mapping fitur kategorikal
    df['fueltype'] = df['fueltype'].map(FUELTYPE_MAP)
    df['aspiration'] = df['aspiration'].map(ASPIRATION_MAP)
    df['doornumber'] = df['doornumber'].map(DOORNUMBER_MAP)
    df['carbody'] = df['carbody'].map(CARBODY_MAP)
    df['drivewheel'] = df['drivewheel'].map(DRIVEWHEEL_MAP)
    df['enginelocation'] = df['enginelocation'].map(ENGINELOCATION_MAP)
    df['enginetype'] = df['enginetype'].map(ENGINETYPE_MAP)
    df['cylindernumber'] = df['cylindernumber'].map(CYLINDERNUMBER_MAP)
    df['fuelsystem'] = df['fuelsystem'].map(FUELSYSTEM_MAP)
    
    # Proses 'CarName' untuk 'compName'
    if 'CarName' in df.columns:
        df['compName'] = df['CarName'].apply(lambda x: x.split(' ')[0])
        df['compName'] = df['compName'].replace(CAR_NAME_CORRECTIONS)
        df['compName'] = df['compName'].map(COMP_NAME_MAP)
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
