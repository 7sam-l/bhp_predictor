import pickle
import json
import numpy as np
import os
from typing import List, Optional, Any

__locations: Optional[List[str]] = None
__data_columns: Optional[List[str]] = None
__model: Any = None

def get_estimated_price(location: str, sqft: float, bhk: int, bath: int) -> float:
    global __data_columns
    global __model

    if __data_columns is None or __model is None:
        load_saved_artifacts()

    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(float(__model.predict([x])[0]), 2)

def load_saved_artifacts() -> None:
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    base_path = os.path.dirname(os.path.abspath(__file__))
    artifacts_dir = os.path.join(base_path, "artifacts")

    with open(os.path.join(artifacts_dir, "columns.json"), "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk

    if __model is None:
        with open(os.path.join(artifacts_dir, 'banglore_home_prices_model.pickle'), 'rb') as f:
            __model = pickle.load(f)
            
    print("loading saved artifacts...done")

def get_location_names() -> List[str]:
    if __locations is None:
        load_saved_artifacts()
    return __locations

def get_data_columns() -> List[str]:
    if __data_columns is None:
        load_saved_artifacts()
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000.0, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000.0, 2, 2))
    print(get_estimated_price('Kalhalli', 1000.0, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000.0, 2, 2))  # other location