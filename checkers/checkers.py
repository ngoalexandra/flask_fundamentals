from flask import Flask, render_template


app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index3.html")

@app.route('/<x>/<y>')
def count(x,y):
    firstNum = int(x)
    secondNum = int(y)
    return render_template("index3.html", x = firstNum, y = secondNum)




app.run(debug = True)