# building a happiness index dashboard

import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for happiness")

df = pd.read_csv("App7/Practice/happy.csv")

choice1 = st.selectbox("Select the data for X-axis",
                     ("GDP", "Happiness", "Generosity"))
choice2 = st.selectbox("Select the data for Y-axis",
                     ("GDP", "Happiness", "Generosity"))

x = df[f"{choice1}".lower()]
y = df[f"{choice2}".lower()]

figure = px.scatter(x=x, y=y,
                    labels={"x":f"{choice1}","y":f"{choice2}"})
st.plotly_chart(figure)
