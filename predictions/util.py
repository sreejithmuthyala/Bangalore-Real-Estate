import json
import pickle
import numpy as np
import sklearn
import os
__locations = None
__data_columns = None
__model = None

def load_saved_artifacts():

    print('loading saved artifacts...start')
    global __data_columns
    global __locations

    # os.path.join(BASE_DIR, 'templates')
   #with open("C:/Users/sreej/Desktop/Telusko/Real Estate Django/Real_estate/predictions/artifacts/columns.json",'r') as f:
    with open("./predictions/artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]
    global __model
   # with open("C:/Users/sreej/Desktop/Telusko/Real Estate Django/Real_estate/predictions/artifacts/bangalore_home_prices_model.pickle",'rb') as f:
    with open("./predictions/artifacts/bangalore_home_prices_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_estimated_price(location,sqft,bhk,bath):
    load_saved_artifacts()
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    # y = __model.predict([x])
    return np.round(__model.predict([x])[0],2)

def get_location_names():
    load_saved_artifacts()
    return __locations

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000,3,3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))
    print(get_estimated_price('Ejipura', 1000, 2, 2))