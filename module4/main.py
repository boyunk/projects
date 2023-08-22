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

@app.route("/")         # the @ symbol means it's a decorator
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>/")
def about(station, date):
    df = pd.read_csv("")
    temperature = df.station(date)
    return {"station": station,
            "date": date,
            "temperature": temperature
            }

if __name__ == "__main__":
    app.run(debug=True)


# runs on port 5000 (it'd be occupied)