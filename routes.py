from app import app
from flask import render_template
from random import randint
from math import factorial

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/random")
def randnum():
    list_ = [randint(1, 100) for i in range(50)]
    list_.sort()
    return render_template("rundnum.html", random=list_)

@app.route("/factorial")
def fact():
    num = randint(0, 100)
    if num < 50: return str(num*1.5)
    else:
        return str(factorial(num))

@app.route("/information")
def te():
    information = {"name": "Zhenia"
                   "country": "Ukrain"
                   "age": "13"}
    return render_template("ftext.html", information=information)
