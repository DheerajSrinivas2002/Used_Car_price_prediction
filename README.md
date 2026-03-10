# 🚗 Used Car Price Predictor

Predicts the price of used cars in the Indian market using XGBoost, achieving a cross-validated MAE of **1.25 Lakhs**.

---

## Why this project

Used car pricing is notoriously opaque in India. Buyers and sellers often have no reliable reference point. This model predicts a fair market price based on key car attributes — brand, power, year, transmission, fuel type and more.

---

## What I built

- Explored and cleaned a real used car dataset with 6019 rows
- Extracted brand from car name using string processing
- Applied **Target Encoding** for Brand (replaced brand names with average price per brand)
- Applied **One Hot Encoding** for Fuel Type
- Applied **Label Encoding** for Location, Transmission and Owner Type
- Trained an **XGBoost Regressor** with hyperparameter tuning via GridSearchCV
- Evaluated using **5-fold Cross Validation**
- Preprocessed a separate test dataset using train's learned encodings
- Built a **Streamlit web app** for live price predictions

---

## Key Results

| Model | MAE | RMSE |
|---|---|---|
| XGBoost baseline | 1.52 Lakhs | 3.65 Lakhs |
| After hyperparameter tuning | 1.41 Lakhs | 3.59 Lakhs |
| After target encoding Brand | **1.25 Lakhs** | **3.21 Lakhs** |

Cross validation scores: [1.13, 1.19, 1.34, 1.18, 1.43] — Avg: **1.25 Lakhs**, Std: **0.11**

---

## Key Insights

- **Brand** (target encoded) was the most important feature — importance score 0.52
- **Power (bhp)** was second most important — 0.14
- **Year** was third — 0.13
- Location and Mileage had minimal impact on price

---

## What I learned

- Difference between Label Encoding, One Hot Encoding and Target Encoding
- Why Target Encoding works better for high-cardinality categorical features
- How to apply the same preprocessing pipeline to test data using train's learned values
- Hyperparameter tuning with GridSearchCV
- Cross validation for reliable model evaluation

---

## Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Matplotlib, Seaborn
- Streamlit
- Joblib

---

## How to Run

```bash
pip install -r requirements.txt
streamlit run car_price_app.py
```

---

## Project Structure

```
├── Data_analysis.ipynb              # EDA and data cleaning
├── Model_training.ipynb             # Model training and evaluation
├── car_price_app.py                 # Streamlit web app
├── car_features.json                # Feature list for model input
├── brand_encoding.json              # Brand target encoding map
├── requirements.txt                 # Dependencies
└── README.md
```

---

## About

Built as part of a self-directed ML learning sprint.  
Mechanical Engineer transitioning into ML/Data Engineering in the Automotive/EV domain.

GitHub: [DheerajSrinivas2002](https://github.com/DheerajSrinivas2002)
