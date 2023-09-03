#Building the GUI for Weather Forecaset Dashboard
import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
# interactive widgits should have variables!
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value =1, max_value =5,
                 help = "Select the number of days")

option = st.selectbox("Select data to view",
                      ("Temperature","Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

data = get_data(place, days, option)

d, t =get_data(days)

figure = px.line(x=d, y= t, labels={"x": "date", "y": "Temperature(F)"})
st.plotly_chart(figure)