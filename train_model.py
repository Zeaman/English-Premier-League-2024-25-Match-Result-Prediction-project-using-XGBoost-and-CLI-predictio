# -----------------------------------
# 🧠 Train Football Result Predictor
# -----------------------------------

# Import dependencies
import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from xgboost import XGBClassifier, plot_importance
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

# -----------------------------
# Load and preview the dataset
# -----------------------------
df = pd.read_csv(r"C:\My_Files\Projects\ep_2024_25_result_prediction\EPL_Results_2024_25.csv")  # Change as per ur dir

print("Initial shape:", df.shape)
print("Available columns:", df.columns.tolist())
print(df.head())

# ---------------------------------------------
# Select relevant 18 features including target
# ---------------------------------------------
features = [
    'FTHG', 'FTAG', 'HS', 'AS', 'HST', 'AST', 'HF', 'AF',
    'HC', 'AC', 'HY', 'AY', 'HR', 'AR',
    'B365H', 'B365D', 'B365A',
    'FTR'  # Target column
]

df = df[features]

# -------------------------------
# Drop rows with any NaN values
# -------------------------------
df.dropna(inplace=True)
print("Cleaned data shape:", df.shape)

# --------------------------
# Encode target column FTR
# --------------------------
# FTR values: 'H', 'D', 'A' → LabelEncoder will map alphabetically: 'A'= 0, 'D'= 1, 'H'= 2

le = LabelEncoder()
df['FTR'] = le.fit_transform(df['FTR'])

# Show mapping
print("Encoded FTR classes:", list(le.classes_))
print("Target distribution:\n", df['FTR'].value_counts())

# --------------------------
# Train-Test Split
# --------------------------
X = df.drop(columns='FTR')
y = df['FTR']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

# --------------------------
# Train XGBoost Classifier
# --------------------------
xgb_model = XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    use_label_encoder=False,
    eval_metric='mlogloss',
    random_state=42
)

xgb_model.fit(X_train, y_train)

# --------------------------
# Evaluation
# --------------------------
y_pred = xgb_model.predict(X_test)

print("\n✅ Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\n📊 Classification Report:")
print(classification_report(y_test, y_pred, target_names=le.classes_))  # Use real labels

# --------------------------
# Feature Importance Plot
# --------------------------
plt.figure(figsize=(10, 8))
plot_importance(xgb_model, max_num_features=10)
plt.title("Top 10 Feature Importances")
plt.tight_layout()
plt.show()

# --------------------------
# Save Model & LabelEncoder
# --------------------------
joblib.dump(xgb_model, r"C:\My_Files\Projects\ep_2024_25_result_prediction\xgb_ftr_model.pkl")  # Change as per ur dir
joblib.dump(le, r"C:\My_Files\Projects\ep_2024_25_result_prediction\ftr_label_encoder.pkl")     # Change as per ur dir

print("\n✅ Model and label encoder saved.")