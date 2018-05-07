from flask import Flask, render_template, request, redirect, session
import random
from random import randint

app = Flask(__name__)
app.secret_key = 'ThisisSecret'


@app.route("/")
def index():
    if "gold" not in session:
        session['gold'] = 0
    return render_template('ninjagold.html')

@app.route('/process_money',  methods=["POST"])
def amount():
    
    if request.form['building'] == 'farm':
        number = random.randint(10,20)
        session['gold'] += number
        return redirect('/')
    elif request.form['building'] == 'cave':
        number = random.randint(5,10)
        session['gold'] += number
        return redirect('/')
    elif request.form['building'] == 'house':
        number = random.randint(2,5)
        session['gold'] += number
        return redirect('/')
    else:
        request.form['building'] == 'casino'
        number = random.randint(0,50)
        if number % 2 == 0:
            session['gold'] += number
        else:
            session['gold'] -= number
        return redirect('/')

        # return redirect('/')

# @app.route("/process_money")
# def getgold():


if __name__ =="__main__":
    app.run(debug =True)

