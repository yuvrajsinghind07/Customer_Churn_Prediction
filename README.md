Customer Churn Prediction


This project focuses on predicting customer churn for a telecom company using machine learning techniques. The goal is to identify customers who are likely to discontinue the service, enabling proactive retention strategies.

Problem Statement

Customer churn significantly impacts business revenue. The objective is to build a predictive model that classifies whether a customer will churn based on demographic, service usage, and billing information.

Dataset

The dataset contains customer-level information including:

Demographics (Gender, SeniorCitizen, Partner, Dependents)

Account details (Tenure, Contract type)

Services subscribed (InternetService, Streaming services, etc.)

Billing information (MonthlyCharges, TotalCharges)

Methodology

Data Cleaning and Preprocessing

Feature Encoding and Scaling using ColumnTransformer

Handling class imbalance using SMOTE

Model building using XGBoost Classifier

Evaluation using classification metrics

Model

Algorithm: XGBoost Classifier

Key Parameters:

n_estimators = 400

learning_rate = 0.05

max_depth = 4

subsample = 0.8

colsample_bytree = 0.8

Performance

Training Accuracy: 0.88

Testing Accuracy: 0.80

Classification Metrics:

Precision (Churn): 0.62

Recall (Churn): 0.65

F1 Score: 0.64

The model demonstrates good generalization with controlled overfitting.

Deployment

The trained model is deployed using Streamlit, allowing users to input customer details and receive real-time churn predictions.

To run the application locally:

streamlit run app.py
Project Structure
Customer_Churn_Prediction/
│
├── app.py
├── churn_model.pkl
├── notebook.ipynb
├── requirements.txt
└── README.md
Key Highlights

End-to-end machine learning pipeline

Integrated preprocessing and model using Pipeline

Handled class imbalance effectively

Deployed as an interactive web application

Author

Yuvraj Singh
Machine Learning Enthusiast
