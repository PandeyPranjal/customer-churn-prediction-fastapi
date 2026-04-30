# app/predict.py

import os
import pickle
import pandas as pd

# -------------------------------
# 📌 Path Handling (Production Safe)
# -------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "model", "customer_churn_model.pkl")
encoder_path = os.path.join(BASE_DIR, "model", "encoders.pkl")

# -------------------------------
# 📌 Load Model + Metadata
# -------------------------------
with open(model_path, "rb") as f:
    model_data = pickle.load(f)

model = model_data["model"]

# Handle both naming cases safely
feature_names = model_data.get("feature_names") or model_data.get("features_names")

if feature_names is None:
    raise ValueError("Feature names not found in model file. Fix your training pipeline.")

# -------------------------------
# 📌 Load Encoders
# -------------------------------
with open(encoder_path, "rb") as f:
    encoders = pickle.load(f)

# -------------------------------
# 📌 Preprocessing Function
# -------------------------------
def preprocess_input(input_data: dict):
    df = pd.DataFrame([input_data])

    # Apply encoding safely
    for column, encoder in encoders.items():
        if column in df.columns:
            val = str(df[column].iloc[0])

            # Handle unseen category safely
            if val in encoder.classes_:
                df[column] = encoder.transform([val])[0]
            else:
                # fallback → first known class
                df[column] = encoder.transform([encoder.classes_[0]])[0]

    # -------------------------------
    # 🔥 Critical: Ensure feature alignment
    # -------------------------------
    try:
        df = df[feature_names]
    except KeyError as e:
        missing_cols = list(set(feature_names) - set(df.columns))
        raise ValueError(f"Missing required input fields: {missing_cols}")

    return df

# -------------------------------
# 📌 Prediction Function
# -------------------------------
def predict_churn(input_data: dict):
    processed = preprocess_input(input_data)

    prediction = model.predict(processed)[0]
    probability = model.predict_proba(processed)[0][1]

    return {
        "churn": int(prediction),
        "probability": float(probability)
    }