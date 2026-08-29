import pickle
import pandas as pd


# Load model
with open("model/loan_model.pkl", "rb") as file:
    model = pickle.load(file)


# Load encoders
with open("model/encoders.pkl", "rb") as file:
    encoders = pickle.load(file)


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


    # Encode categorical columns
    categorical_columns = [
        "Gender",
        "Married",
        "Dependents",
        "Education",
        "Self_Employed",
        "Property_Area"
    ]

    for col in categorical_columns:
        df[col] = encoders[col].transform(df[col])


    # Convert numeric columns
    df["Loan_Amount_Term"] = pd.to_numeric(
        df["Loan_Amount_Term"]
    )

    df["Credit_History"] = pd.to_numeric(
        df["Credit_History"]
    )


    # IMPORTANT:
    # Keep exactly the same order used during training
    df = df[model.feature_names_in_]


    # Prediction
    prediction = model.predict(df)[0]


    if prediction == 1:
        return "Loan Approved"
    else:
        return "Loan Rejected"