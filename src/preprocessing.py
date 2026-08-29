from pathlib import Path

import pandas as pd

# PATHS


BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"

DATA_PATH = DATA_DIR / "train.csv"

# FEATURES


FEATURES = [
    "Gender",
    "Married",
    "Dependents",
    "Education",
    "Self_Employed",
    "Loan_Amount_Term",
    "Credit_History",
    "Property_Area"
]

TARGET = "Loan_Status"



# LOAD DATA


def load_data():

    data = pd.read_csv(DATA_PATH)

    return data



# PREPARE DATA


def prepare_data():

    data = load_data()

    # Keep only required columns
    data = data[FEATURES + [TARGET]].copy()

    # Handle missing values
    data["Gender"] = data["Gender"].fillna("Male")

    data["Married"] = data["Married"].fillna("No")

    data["Dependents"] = data["Dependents"].fillna("0")

    data["Education"] = data["Education"].fillna("Graduate")

    data["Self_Employed"] = data["Self_Employed"].fillna("No")

    data["Loan_Amount_Term"] = data["Loan_Amount_Term"].fillna(
        data["Loan_Amount_Term"].median()
    )

    data["Credit_History"] = data["Credit_History"].fillna(1)

    data["Property_Area"] = data["Property_Area"].fillna("Urban")

    # Convert target
    data[TARGET] = data[TARGET].map({
        "Y": 1,
        "N": 0
    })

    return data