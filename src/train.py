import pickle
from pathlib import Path

from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from data_pre_processing import load_data, split_data

ROOT_DIR = Path(__file__).resolve().parents[1]
MODEL_DIR = ROOT_DIR / "model"
MODEL_DIR.mkdir(exist_ok=True)

X, Y, encoders = load_data()

x_train, x_test, y_train, y_test = split_data(X, Y)

model = Pipeline([
    ("Scaler", StandardScaler()),
    ("model", LogisticRegression(max_iter=1000))
])

model.fit(x_train, y_train)

with (MODEL_DIR / "loan_model.pkl").open("wb") as file:
    pickle.dump(model, file)

with (MODEL_DIR / "encoders.pkl").open("wb") as file:
    pickle.dump(encoders, file)

print("model trained successfully")

