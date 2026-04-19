import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from model import predict_marks

st.title("🎓 Student Performance Prediction System")
st.write("Enter your study details to predict your marks 📊")

# load dataset
data = pd.read_csv("C:\\Users\\Nishita\\Downloads\\CS\\Student Performace Predictor\\data.csv")

# inputs
hours = st.slider("Hours Studied", 0, 12, 5)
attendance = st.slider("Attendance (%)", 0, 100, 75)
sleep = st.slider("Sleep Hours", 0, 10, 6)

# prediction
if st.button("Predict"):
    if hours == 0:
        st.warning("Please enter valid study hours")
    else:
        result = predict_marks(hours, attendance, sleep)
        st.success(f"Predicted Marks: {round(result, 2)}")

        # 📈 GRAPH
        st.write("### 📈 Visualization")

        fig, ax = plt.subplots()

        # smooth curve
        x_vals = np.linspace(0, 12, 100)
        y_vals = [predict_marks(x, attendance, sleep) for x in x_vals]

        ax.plot(x_vals, y_vals)

        # actual data points
        ax.scatter(data['hours'], data['marks'], alpha=0.6)

        # your prediction point
        ax.scatter(hours, result)
        ax.legend()

        ax.set_xlabel("Hours Studied")
        ax.set_ylabel("Marks")
        ax.set_title("Effect of Study Hours on Marks")

        st.pyplot(fig)

# insights
st.write("### 📈 Insights:")
st.write("- More study hours generally increase marks")
st.write("- Good attendance improves performance")
st.write("- Proper sleep helps learning efficiency")
