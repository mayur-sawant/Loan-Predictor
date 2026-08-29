import pickle

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from data_pre_processing import load_data,split_data

X,Y,encoders = load_data()

x_train,x_test,y_train,y_test = split_data(X,Y)

model = Pipeline([
    ("Scaler",StandardScaler()),
    ("model",LogisticRegression(max_iter=1000))
])

model.fit(x_train,y_train)

with open("model/loan_model.pkl","wb") as file:
    pickle.dump(model,file)

with open("model/encoders.pkl","wb") as file:
    pickle.dump(encoders, file)

print("model trained successfully")

