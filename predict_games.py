# --------------------------
# predict_game.py
# --------------------------

import pandas as pd
import joblib
import argparse

# --------------------------
# Step 1: Load Trained Model & LabelEncoder
# --------------------------
model_path = r"C:\My_Files\Projects\ep_2024_25_result_prediction\xgb_ftr_model.pkl"         # Change as per ur dir
encoder_path = r"C:\My_Files\Projects\ep_2024_25_result_prediction\ftr_label_encoder.pkl"   # Change as per ur dir

model = joblib.load(model_path)
label_encoder = joblib.load(encoder_path)

# --------------------------
# Step 2: Parse CLI Arguments
# --------------------------
parser = argparse.ArgumentParser(description="Predict football match result using XGBoost model")
parser.add_argument('--features', nargs=17, type=float, required=True,
                    help='Provide exactly 17 feature values: FTHG FTAG HS AS HST AST HF AF HC AC HY AY HR AR B365H B365D B365A')
args = parser.parse_args()

# --------------------------
# Step 3: Format Input Data
# --------------------------
input_features = [
    'FTHG', 'FTAG', 'HS', 'AS', 'HST', 'AST', 'HF', 'AF',
    'HC', 'AC', 'HY', 'AY', 'HR', 'AR',
    'B365H', 'B365D', 'B365A'
]

input_data = pd.DataFrame([args.features], columns=input_features)

# --------------------------
# Step 4: Predict
# --------------------------
pred = model.predict(input_data)
pred_label = label_encoder.inverse_transform(pred)[0]  # Get 'H', 'D', or 'A'

# Map to readable label
readable_mapping = {'H': 'Home_win', 'D': 'Draw', 'A': 'Away_win'}
output = readable_mapping.get(pred_label, 'Unknown')

print(f"\n📊 Predicted Match Result: {output}")