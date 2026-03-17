import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline model
model = joblib.load("churn_model.pkl")

st.title("Customer Churn Prediction")

st.write("Enter customer details")


gender = st.selectbox("Gender", ["Male", "Female"])

SeniorCitizen = st.selectbox("Senior Citizen", [0,1])

Partner = st.selectbox("Partner", ["Yes","No"])

Dependents = st.selectbox("Dependents", ["Yes","No"])

tenure = st.slider("Tenure (months)",0,72,12)

PhoneService = st.selectbox("Phone Service", ["Yes","No"])

MultipleLines = st.selectbox("Multiple Lines", ["No","Yes","No phone service"])

InternetService = st.selectbox("Internet Service", ["DSL","Fiber optic","No"])

OnlineSecurity = st.selectbox("Online Security", ["Yes","No","No internet service"])

OnlineBackup = st.selectbox("Online Backup", ["Yes","No","No internet service"])

DeviceProtection = st.selectbox("Device Protection", ["Yes","No","No internet service"])

TechSupport = st.selectbox("Tech Support", ["Yes","No","No internet service"])

StreamingTV = st.selectbox("Streaming TV", ["Yes","No","No internet service"])

StreamingMovies = st.selectbox("Streaming Movies", ["Yes","No","No internet service"])

Contract = st.selectbox("Contract", ["Month-to-month","One year","Two year"])

PaperlessBilling = st.selectbox("Paperless Billing", ["Yes","No"])

PaymentMethod = st.selectbox("Payment Method",
["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])

MonthlyCharges = st.number_input("Monthly Charges")

TotalCharges = st.number_input("Total Charges")



input_data = pd.DataFrame({

"gender":[gender],
"SeniorCitizen":[SeniorCitizen],
"Partner":[Partner],
"Dependents":[Dependents],
"tenure":[tenure],
"PhoneService":[PhoneService],
"MultipleLines":[MultipleLines],
"InternetService":[InternetService],
"OnlineSecurity":[OnlineSecurity],
"OnlineBackup":[OnlineBackup],
"DeviceProtection":[DeviceProtection],
"TechSupport":[TechSupport],
"StreamingTV":[StreamingTV],
"StreamingMovies":[StreamingMovies],
"Contract":[Contract],
"PaperlessBilling":[PaperlessBilling],
"PaymentMethod":[PaymentMethod],
"MonthlyCharges":[MonthlyCharges],
"TotalCharges":[TotalCharges]

})



if st.button("Predict"):

    prediction = model.predict(input_data)
    prob = model.predict_proba(input_data)

    if prediction[0] == 1:
        st.error("Yes! Customer will Churn")
    else:
        st.success("No! Customer will not churn")

    st.write("Churn Probability:",prob[0][1])