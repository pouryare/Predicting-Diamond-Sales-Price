import joblib
import numpy as np
import pandas as pd
from pathlib import Path

__version__ = "2.0.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

# Load the trained model
model = joblib.load(f'{BASE_DIR}/best_model.joblib')

# Extract feature names from the model
model_features = model.feature_names_in_.tolist()

numeric_features = ['carat_weight', 'depth_percent', 'table_percent', 'meas_length', 'meas_width', 'meas_depth']

def preprocess_data(input_data):
    df = pd.DataFrame([input_data])
    
    # Convert numeric features to float
    for feature in numeric_features:
        df[feature] = pd.to_numeric(df[feature], errors='coerce')
    
    # Load and apply label encoders for categorical features
    categorical_features = [f for f in model_features if f not in numeric_features]
    for feature in categorical_features:
        try:
            le = joblib.load(f'{BASE_DIR}/{feature}_encoder.joblib')
            df[feature] = le.transform(df[feature].astype(str))
        except Exception:
            df[feature] = 0  # Set a default value if encoding fails
    
    # Feature engineering
    df['volume'] = df['meas_length'] * df['meas_width'] * df['meas_depth']
    df['aspect_ratio'] = df['meas_length'] / df['meas_width']
    
    # Ensure all features are present and in the correct order
    for feature in model_features:
        if feature not in df.columns:
            df[feature] = 0  # or some appropriate default value
    
    # Select only the features used in training
    return df[model_features]

def predict_price(input_data):
    try:
        processed_data = preprocess_data(input_data)
        prediction = model.predict(processed_data)
        return prediction[0]
    except Exception as e:
        raise ValueError(f"Prediction error: {str(e)}")