import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

details = [
    "Gender",
    "Married",
    "Dependents",
    "Education",
    "Self_Employed",
    "Loan_Amount_Term",
    "Property_Area",
    "Credit_History"
]

def load_data():
    data = pd.read_csv("data/train.csv")

    

    encoders = {}

    for col in data.select_dtypes(include = "object").columns:
        encoder = LabelEncoder()
        data[col] = encoder.fit_transform(data[col].astype(str))
        encoders[col] = encoder

    X = data[details]
    X = X.ffill().bfill()

    Y= data["Loan_Status"]

    return X, Y, encoders

def split_data(X,Y):
    dt = train_test_split(X,Y, test_size=0.2,random_state=42)
    return dt
