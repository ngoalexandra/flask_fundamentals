from flask import Flask, render_template


app = Flask(__name__)
@app.route('/play')
def index():
    return render_template("index2.html", )

@app.route('/play/<idx>')
def numoftimes(idx):
    temp = int(idx)
    return render_template("index2.html", boxNum = temp)

@app.route('/play/<idx>/<color>')
def color(idx,color):
    temp = int(idx)
    return render_template("index2.html", boxNum = temp, colors = color)



app.run(debug = True)