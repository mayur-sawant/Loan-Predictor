import pandas as pd

from src.predictor import predict_loan


def preprocess_input(
    gender,
    married,
    dependents,
    education,
    self_employed,
    loan_amount_term,
    credit_history,
    property_area
):

    # Create dataframe
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

    return df


def validate_input(
    gender,
    married,
    dependents,
    education,
    self_employed,
    loan_amount_term,
    credit_history,
    property_area
):

    errors = []

    # Gender
    if gender not in ["Male", "Female"]:
        errors.append("Please select a valid gender.")

    # Married
    if married not in ["Yes", "No"]:
        errors.append("Please select marital status.")

    # Dependents
    if dependents not in ["0", "1", "2", "3+"]:
        errors.append("Please select a valid number of dependents.")

    # Education
    if education not in ["Graduate", "Not Graduate"]:
        errors.append("Please select education.")

    # Self employed
    if self_employed not in ["Yes", "No"]:
        errors.append("Please select self-employment status.")

    # Loan term
    if loan_amount_term is None:
        errors.append("Loan amount term is required.")

    elif loan_amount_term <= 0:
        errors.append("Loan amount term must be greater than 0.")

    # Credit history
    if credit_history not in [0, 1]:
        errors.append("Credit history must be 0 or 1.")

    # Property area
    if property_area not in [
        "Urban",
        "Semiurban",
        "Rural"
    ]:
        errors.append("Please select a valid property area.")

    return errors


def process_and_predict(
    gender,
    married,
    dependents,
    education,
    self_employed,
    loan_amount_term,
    credit_history,
    property_area
):

    # Validate
    errors = validate_input(
        gender,
        married,
        dependents,
        education,
        self_employed,
        loan_amount_term,
        credit_history,
        property_area
    )

    if errors:
        return None, errors


    # Preprocess
    df = preprocess_input(
        gender,
        married,
        dependents,
        education,
        self_employed,
        loan_amount_term,
        credit_history,
        property_area
    )


    # Use existing prediction function
    prediction = predict_loan(
        gender,
        married,
        dependents,
        education,
        self_employed,
        loan_amount_term,
        credit_history,
        property_area
    )

    return prediction, []