import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("fraud_detection_pipeline.pkl")

st.title("Fraud Detection Prediction App")
st.markdown("Please Enter the Transaction details and Use the Prediction button")
st.divider()

# Inputs
transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASHOUT", "DEPOSIT"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0, key="amount")
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0, key="oldbalanceOrg")
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0, key="newbalanceOrig")
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0, key="oldbalanceDest")
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0, key="newbalanceDest")

# Prediction
if st.button("Predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction: {int(prediction)}")

    if prediction == 1:
        st.error("⚠️ This Transaction may be Fraudulent")
    else:
        st.success("✅ This Transaction looks Legitimate")
