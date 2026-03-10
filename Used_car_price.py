import streamlit as st
import joblib
import json
import pandas as pd

# Load model and files
model = joblib.load('car_price_model.pkl')

with open('car_features.json', 'r') as f:
    features = json.load(f)

with open('brand_encoding.json', 'r') as f:
    brand_encoding = json.load(f)

# App title
st.title("🚗 Used Car Price Predictor")
st.markdown("Predict the price of a used car in the Indian market")

st.sidebar.header("Car Details")

# Brand selector
brand_list = sorted(brand_encoding.keys())
selected_brand = st.sidebar.selectbox("Brand", brand_list)
brand_encoded = brand_encoding[selected_brand]

# Other inputs
year = st.sidebar.slider("Year", 2000, 2024, 2018)
km_driven = st.sidebar.slider("Kilometers Driven", 0, 300000, 50000)
mileage = st.sidebar.slider("Mileage (kmpl)", 5.0, 35.0, 18.0)
engine = st.sidebar.slider("Engine (CC)", 500, 5000, 1200)
power = st.sidebar.slider("Power (bhp)", 30.0, 500.0, 100.0)
seats = st.sidebar.slider("Seats", 2, 9, 5)

transmission = st.sidebar.selectbox("Transmission", ["Manual", "Automatic"])
owner_type = st.sidebar.selectbox("Owner Type", ["First", "Second", "Third", "Fourth & Above"])
location = st.sidebar.selectbox("Location", ["Mumbai", "Delhi", "Bangalore", "Chennai",
                                               "Hyderabad", "Pune", "Kolkata", "Jaipur",
                                               "Coimbatore", "Kochi", "Ahmedabad"])
fuel_type = st.sidebar.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])

# Encode categorical inputs
transmission_enc = 1 if transmission == "Manual" else 0
owner_map = {"First": 0, "Second": 1, "Third": 2, "Fourth & Above": 3}
owner_enc = owner_map[owner_type]
location_map = {"Ahmedabad": 0, "Bangalore": 1, "Chennai": 2, "Coimbatore": 3,
                "Delhi": 4, "Hyderabad": 5, "Jaipur": 6, "Kochi": 7,
                "Kolkata": 8, "Mumbai": 9, "Pune": 10}
location_enc = location_map[location]

fuel_diesel = 1 if fuel_type == "Diesel" else 0
fuel_electric = 1 if fuel_type == "Electric" else 0
fuel_lpg = 1 if fuel_type == "LPG" else 0
fuel_petrol = 1 if fuel_type == "Petrol" else 0

# Build input in EXACT feature order
input_data = pd.DataFrame([[
    location_enc,    # Location
    year,            # Year
    km_driven,       # Kilometers_Driven
    transmission_enc,# Transmission
    owner_enc,       # Owner_Type
    mileage,         # Mileage
    engine,          # Engine
    power,           # Power
    seats,           # Seats
    brand_encoded,   # Brand_encoded
    fuel_diesel,     # Fuel_Type_Diesel
    fuel_electric,   # Fuel_Type_Electric
    fuel_lpg,        # Fuel_Type_LPG
    fuel_petrol      # Fuel_Type_Petrol
]], columns=features)

# Predict
prediction = model.predict(input_data)[0]

# Display result
st.metric(
    label="Predicted Price",
    value=f"₹ {prediction:.2f} Lakhs"
)

# Context
if prediction < 5:
    st.success("✅ Budget segment")
elif prediction < 15:
    st.info("ℹ️ Mid range segment")
elif prediction < 30:
    st.warning("⚠️ Premium segment")
else:
    st.error("💎 Luxury segment")