# ⚽ EPL 2024/25 Match Result Predictor (XGBoost)

This project predicts the full-time result (`FTR`) of English Premier League (EPL) 2024/25 matches based on match statistics and betting odds using an **XGBoost Classifier**.

## 📁 Get Dataset:

https://www.football-data.co.uk/englandm.php

Prediction target:
- `H` → Home Win
- `D` → Draw
- `A` → Away Win

📦 Currently supports CLI-based predictions. A web dashboard and confidence-based outputs are **in development**.

---

## 📁 Project Structure

ep_2024_25_result_prediction/
│
├── EPL_Results_2024_25.csv # Dataset (cleaned with 18 relevant features)
├── train_model.py # Model training script
├── predict_game.py # Command-line prediction script
├── xgb_ftr_model.pkl # Trained XGBoost model
├── ftr_label_encoder.pkl # LabelEncoder used to encode/decode FTR labels
└── README.md # Project documentation


---

## 📊 Features Used for Prediction

The model uses the following 17 match statistics and odds features:

| Feature   | Description |
|-----------|-------------|
| `FTHG`    | Full Time Home Goals |
| `FTAG`    | Full Time Away Goals |
| `HS`      | Home Shots |
| `AS`      | Away Shots |
| `HST`     | Home Shots on Target |
| `AST`     | Away Shots on Target |
| `HF`      | Home Fouls |
| `AF`      | Away Fouls |
| `HC`      | Home Corners |
| `AC`      | Away Corners |
| `HY`      | Home Yellow Cards |
| `AY`      | Away Yellow Cards |
| `HR`      | Home Red Cards |
| `AR`      | Away Red Cards |
| `B365H`   | Bet365 Odds - Home Win |
| `B365D`   | Bet365 Odds - Draw |
| `B365A`   | Bet365 Odds - Away Win |


## 🏗️ Training the Model

> Skip this if you're only using the CLI predictor.

### 🔧 Step-by-Step:

1. Make sure the `EPL_Results_2024_25.csv` dataset has the columns listed above, including `FTR` (actual full-time result).

2. Run the training script:

```bash
python train_model.py

### 🎯 Making Predictions via CLI`

```bash
python predict_game.py --features <17 float values>

Example:

```bash
python predict_game.py --features 1 0 12 10 5 3 8 9 5 7 1 2 0 0 2.1 3.0 3.4

📊 Output:
```bash
Predicted Match Result: Away_win

### 📈 Model Details

Algorithm: XGBoost Classifier

Label Encoding:

H → Home win

D → Draw

A → Away win

Evaluation:

Confusion matrix and classification report on 20% test split

Top 10 feature importance chart

### 🛠️ Installation

✅ Prerequisites
Python 3.8+

Install dependencies:

```bash
pip install pandas matplotlib scikit-learn xgboost joblib

### 🚧 In Development

Feature		
| Feature               | Status        | Notes  | 
|-----------------------|-----------    | ------ |
|`Web UI (EXE/Flask)`	    |🔄 Ongoing	    | User-friendly input + prediction interface|
|`Probability Output`	    |🔄 Planned     | Add model.predict_proba() to show win/draw/loss confidence|
|`Batch CSV Predictions`	|🔄 Planned	    | Load match data CSV → output results in bulk|
|`Hyperparameter Tuning`	|⏳ Todo	      | Improve accuracy with GridSearchCV or Optuna|
|`League Generalization`	|⏳ Todo	      | Extend model to support multiple leagues (La Liga, Serie A, etc.)|
|`REST API`	              |🔄 Planned	    | Make predictions over HTTP requests (FastAPI or Flask-based API)|
|`Dockerization`	        |⏳ Todo	      | Containerize for reproducibility and deployment|


