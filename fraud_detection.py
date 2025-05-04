import streamlit as st
import pandas as pd
import numpy as np
import joblib

model= joblib.load("fraud_detection_Pipeline.pkl")

st.title("Fraud Detection App")

st.markdown("please enter the transaction details below and click on the button to check if the transaction is fraudulent or not.")

st.divider()

transaction_type=st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER","CASH_OUT","DEPOSIT"])
amount=st.number_input("Transaction Amount", min_value=0.0, step=500.0)  
oldbalanceOrg=st.number_input("Old Balance (sender)", min_value=0.0, value=10000.0)
newbalanceOrig=st.number_input("New Balance (sender)", min_value=0.0, value=9000.0)
oldbalanceDest=st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest=st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

if st.button("predict"):
    # Create a DataFrame with the input data
    input_data = pd.DataFrame({
        'type': [transaction_type],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest]
    })
    
    # Make prediction
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.error("The transaction is fraudulent.")
    else:
        st.success("The transaction is not fraudulent.")