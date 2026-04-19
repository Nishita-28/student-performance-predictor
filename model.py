import pandas as pd
from sklearn.linear_model import LinearRegression

# load data
data = pd.read_csv("data.csv")

X = data[['hours', 'attendance', 'sleep']]
y = data['marks']

# train model
model = LinearRegression()
model.fit(X, y)

# function to predict
def predict_marks(hours, attendance, sleep):
    return model.predict([[hours, attendance, sleep]])[0]
