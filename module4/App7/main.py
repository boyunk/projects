#Building the GUI for Weather Forecaset Dashboard
import streamlit as st
import plotly.express as px
from backend import get_data

# Add a title, text input, slider, selectbox, and subheader
st.title("Weather Forecast for the Next Days")
# interactive widgits should have variables!
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value =1, max_value =5,
                 help = "Select the number of days")

option = st.selectbox("Select data to view",
                      ("Temperature","Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

# fix the error that appears when the place is not inserted
    if place:

    # get the temperature/sky data
    filtered_data = get_data(place, days)

    if option = "temperature":
        # moving the filtering process to main to be processed once the temperature option is selected
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
        # list comprehension for date
        dates = [dict["dt.txt"] for dict in filtered_data]
        # create a temperature plot
        figure = px.line(x=d, y= temperature, labels={"x": "date", "y": "Temperature(F)"})
        st.plotly_chart(figure)


    if option = "Sky":
        # creating a dictionary for sky coniditions and images
        # Option 1: use for loops
        #sky_conditions = ["Clear", "Clouds", "Rain", "Snow"]
        #sky_dict = {}
        #for conditions in sky_conditions:
        #    image_path = f"images/{sky_conditions}.png"
        #    sky_dict[condition] = image_path

        # Option 2: use list comprehension
        sky = ["clear", "cloud", "rain", "snow"]
        images = {condition: f"images/{condition}.png" for condition in sky}

        # moving code from backend to front
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        print(sky_conditions)
        st.image(image_paths, width = 115)
