# this api returns the definition of words

# returns definition in capital letters, word itself for today
import pandas as pd
from flask import Flask, render_template

app = Flask("__name__")


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<word>")
def about(word):
    #df = pd.read_csv("")
    definition = word.upper()
    return{"definition":definition,
           "word": word
           }

if __name__ == "__main__":
    app.run(debug=True, port=5001)