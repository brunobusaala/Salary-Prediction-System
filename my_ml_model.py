import joblib
import json
import sys


def load_model(model_path):
    return joblib.load(model_path)


def predict(model, input_data):
    prediction = model.predict(input_data)
    result = {"PredictedSalary": prediction.tolist()}
    print(json.dumps(result))  # Print the JSON result
    sys.stdout.flush()  # Flush the output
