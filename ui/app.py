import streamlit as st
import requests

st.title("🏡 Housing Price Predictor")

# Input fields
col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Area", value=5000)
    bedrooms = st.slider("Bedrooms", 1, 6, 3)
    bathrooms = st.slider("Bathrooms", 1, 4, 1)
    stories = st.slider("Stories", 1, 4, 1)
    parking = st.slider("Parking Spaces", 0, 3, 1)

with col2:
    mainroad = st.selectbox("Mainroad", ["yes", "no"])
    guestroom = st.selectbox("Guestroom", ["yes", "no"])
    basement = st.selectbox("Basement", ["yes", "no"])
    hotwater = st.selectbox("Hot Water Heating", ["yes", "no"])
    ac = st.selectbox("Air Conditioning", ["yes", "no"])
    prefarea = st.selectbox("Preferred Area", ["yes", "no"])
    furnishing = st.selectbox("Furnishing", ["furnished", "semi-furnished", "unfurnished"])

if st.button("Predict Price"):
    payload = {
        "area": area, "bedrooms": bedrooms, "bathrooms": bathrooms,
        "stories": stories, "mainroad": mainroad, "guestroom": guestroom,
        "basement": basement, "hotwaterheating": hotwater, "airconditioning": ac,
        "parking": parking, "prefarea": prefarea, "furnishingstatus": furnishing
    }
    
    response = requests.post("http://localhost:8000/predict", json=payload)
    if response.status_code == 200:
        price = response.json()["estimated_price"]
        st.success(f"Estimated House Price: ₹{price:,.2f}")
    else:
        st.error("Error in prediction API")