# ⚽ EPL 2024/25 Match Result Predictor (XGBoost)

> Skip this if you're only using the CLI predictor.

### 🔧 Step-by-Step Training:

1. Make sure the `EPL_Results_2024_25.csv` dataset has the required columns, including `FTR` (actual full-time result).

2. Run the training script:

```bash
python train_model.py
```

### 🎯 Making Predictions via CLI

```bash
python predict_game.py --features <17 float values>
```

Example:

```bash
python predict_game.py --features 1 0 12 10 5 3 8 9 5 7 1 2 0 0 2.1 3.0 3.4
```

📊 Output:
```bash
Predicted Match Result: Away_win
```

### 📈 Model Details

- **Algorithm**: XGBoost Classifier  
- **Label Encoding**:
  - H → Home win
  - D → Draw  
  - A → Away win  
- **Evaluation**:
  - Confusion matrix and classification report on 20% test split
  - Top 10 feature importance chart  

### 🛠️ Installation

✅ **Prerequisites**  
Python 3.8+  

Install dependencies:
```bash
pip install pandas matplotlib scikit-learn xgboost joblib
```

### 🚧 In Development

| Feature                   | Status        | Notes  |
|---------------------------|---------------|--------|
| Web UI (Flask) and EXE    | 🔄 Ongoing    | User-friendly input + prediction interface |
| Probability Output        | 🔄 Planned    | Add model.predict_proba() to show win/draw/loss confidence |
| Batch CSV Predictions     | 🔄 Planned    | Load match data CSV → output results in bulk |
| Hyperparameter Tuning     | ⏳ Todo       | Improve accuracy with GridSearchCV or Optuna |
| League Generalization     | ⏳ Todo       | Extend model to support multiple leagues (La Liga, Serie A, etc.) |
| REST API                  | 🔄 Planned    | Make predictions over HTTP requests (FastAPI or Flask-based API) |
| Dockerization             | ⏳ Todo       | Containerize for reproducibility and deployment |

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

MIT License

Copyright (c) 2025 Amanuel Mihiret

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
In the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS ARE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OF OTHER DEALINGS IN THE
SOFTWARE.

## Contact

Amanuel Mihiret (MSc. in Mechatronics Engineering)
zeaman44@gmail.com,
amanmih@dtu.edu.et
```


