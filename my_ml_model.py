# my_ml_model.py

import joblib

def load_model(model_path):
    return joblib.load(model_path)

def predict(model, input_data):
    return model.predict(input_data)
