# building a happiness index dashboard

import streamlit as st
import plotly.express as px
import pandas as pd

# add title to widget
st.title("In Search for happiness")


# add select boxes
choice1 = st.selectbox("Select the data for X-axis",
                     ("GDP", "Happiness", "Generosity"))
choice2 = st.selectbox("Select the data for Y-axis",
                     ("GDP", "Happiness", "Generosity"))

# load data
df = pd.read_csv("App7/Practice/happy.csv")

# match the value of first option
match choice1:
    case "Happiness":
        x_array = df["happiness"]
    case "GDP":
        x_array = df["gdp"]
    case "GDP":
        x_array = df["gdp"]

# match the value of second option
match choice2:
    case "Happiness":
        y_array = df["happiness"]
    case "GDP":
        y_array = df["gdp"]
    case "GDP":
        y_array = df["gdp"]

#add subheader for the plot
st.subheader(f"{choice1} and {choice2}")
figure = px.scatter(x=x_array, y=y_array,
                    labels={"x": choice1,"y": choice2})
st.plotly_chart(figure)
