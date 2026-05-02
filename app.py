import streamlit as st
import numpy as np
import joblib

# Load trained model
rf = joblib.load("model.pkl")

# Title
st.title("💳 Credit Card Fraud Detection")
st.subheader("Check if a transaction is risky")

st.markdown("Enter transaction details below:")

# Inputs
distance = st.slider("Distance from home (km)", 0.0, 100.0, 10.0)

amount = st.number_input("Transaction amount (₹)", min_value=1.0)

usual_amount = st.number_input("Your usual spending (₹)", min_value=1.0)

online = st.radio("Is this an online transaction?", ["Yes", "No"])
chip = st.radio("Was chip used?", ["Yes", "No"])
pin = st.radio("Was PIN used?", ["Yes", "No"])
repeat = st.radio("Have you used this retailer before?", ["Yes", "No"])

# Convert inputs safely
ratio = amount / usual_amount if usual_amount != 0 else 0

online = 1 if online == "Yes" else 0
chip = 1 if chip == "Yes" else 0
pin = 1 if pin == "Yes" else 0
repeat = 1 if repeat == "Yes" else 0

# Prediction
if st.button("Check Fraud"):
    input_data = np.array([[distance, 0, ratio, repeat, chip, pin, online]])
    
    prob = rf.predict_proba(input_data)[0][1]

    st.write(f"### Fraud Probability: {round(prob*100,2)}%")

    # Progress bar (visual impact)
    st.progress(float(prob))

    if prob > 0.7:
        st.error("⚠️ High Fraud Risk")
    elif prob > 0.4:
        st.warning("⚠️ Moderate Risk")
    else:
        st.success("✅ Low Risk")
