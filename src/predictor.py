from pathlib import Path
import pickle

import pandas as pd


# PATH


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "model" / "loan_model.pkl"


# LOAD MODEL


with open(MODEL_PATH, "rb") as file:

    model = pickle.load(file)


# PREDICTION FUNCTION


def predict_loan(
    gender,
    married,
    dependents,
    education,
    self_employed,
    loan_amount_term,
    credit_history,
    property_area
):

    data = {

        "Gender": [gender],

        "Married": [married],

        "Dependents": [dependents],

        "Education": [education],

        "Self_Employed": [self_employed],

        "Loan_Amount_Term": [loan_amount_term],

        "Credit_History": [credit_history],

        "Property_Area": [property_area]

    }


    df = pd.DataFrame(data)


    prediction = model.predict(df)[0]


    probability = model.predict_proba(df)[0]


    if prediction == 1:

        result = "Loan Approved"

        confidence = probability[1]

    else:

        result = "Loan Rejected"

        confidence = probability[0]


    return result, confidence