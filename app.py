import xdrlib
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    from var import x
    from var import username_check
    return render_template('home.html',username_check(x))

@app.route("/page2")
def page2():
    return render_template("page2.html")

