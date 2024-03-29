# Data analysis and visualization module
# use pandas, maploblib, plotly

# learn how to build api
# use html

# this step builds the webframe
from flask import Flask, render_template
import pandas as pd

app = Flask("__name__")

# each web page should be in templates folder
# images should be in static folder

variable = "Hello There"
stations = pd.read_csv("data_small/stations.txt", skiprows = 17)
stations = stations[["STAID","STANAME                                 "]]
@app.route("/")         # the @ symbol means it's a decorator
def home():
    return render_template("home.html", data = stations.to_html())

@app.route("/api/v1/<station>/<date>/")
def about(station, date):
    filename = ("data_small/TG_STAID"+str(station).zfill(6)+".txt")
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE']== date]['   TG'].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature
            }

# making data visible for all data for a certain station & for a year

@app.route("/api/v1/<station>/")
def all_data(station):
    filename = ("data_small/TG_STAID"+str(station).zfill(6)+".txt")
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict(orient = "records")
    return result@app.route("/api/v1/<station>/")

@app.route("/api/v1/yearly/<station>/<year>/")
def annual_data(station, year):
    filename = ("data_small/TG_STAID"+str(station).zfill(6)+".txt")
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    result = df[df["    DATE"].str.startswith(str(year))].to_dict(orient = "records")
    return result


if __name__ == "__main__":
    app.run(debug=True)


# runs on port 5000 (it'd be occupied)
# station
