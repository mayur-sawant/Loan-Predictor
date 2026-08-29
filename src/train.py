from pathlib import Path
import pickle

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression

from src.preprocessing import (
    prepare_data,
    FEATURES
)

# PATHS


BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_DIR = BASE_DIR / "model"

MODEL_PATH = MODEL_DIR / "loan_model.pkl"


# LOAD DATA


data = prepare_data()


X = data[FEATURES]

y = data["Loan_Status"]


# COLUMN TYPES

categorical_features = [
    "Gender",
    "Married",
    "Dependents",
    "Education",
    "Self_Employed",
    "Property_Area"
]


numeric_features = [
    "Loan_Amount_Term",
    "Credit_History"
]


# CATEGORICAL PIPELINE

categorical_pipeline = Pipeline([
    (
        "imputer",
        SimpleImputer(strategy="most_frequent")
    ),

    (
        "encoder",
        OneHotEncoder(
            handle_unknown="ignore"
        )
    )
])


# NUMERIC PIPELINE


numeric_pipeline = Pipeline([
    (
        "imputer",
        SimpleImputer(strategy="median")
    ),

    (
        "scaler",
        StandardScaler()
    )
])


# PREPROCESSOR


preprocessor = ColumnTransformer([

    (
        "categorical",
        categorical_pipeline,
        categorical_features
    ),

    (
        "numeric",
        numeric_pipeline,
        numeric_features
    )

])


# MODEL


model = Pipeline([

    (
        "preprocessor",
        preprocessor
    ),

    (
        "classifier",
        LogisticRegression(
            max_iter=1000
        )
    )

])


# TRAIN


print("Training model...")

model.fit(X, y)


# SAVE MODEL


MODEL_DIR.mkdir(
    parents=True,
    exist_ok=True
)


with open(MODEL_PATH, "wb") as file:

    pickle.dump(
        model,
        file
    )


print("Model trained successfully.")

print(
    f"Model saved to: {MODEL_PATH}"
)