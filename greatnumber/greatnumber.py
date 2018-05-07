from flask import Flask, render_template, request, redirect, session
import random
from random import randint

app = Flask(__name__)
app.secret_key = 'ThisIsSecret' 

randomNum = random.randint(1,101)

@app.route('/')
def index():
    if 'number' not in session:
        session['number'] = randomNum 
    return render_template('greatnumber.html')
@app.route('/random', methods=["POST"])
def guesses():
    if int(request.form['guess']) < randomNum:
        return("Too Low! Try Again!")
    if int(request.form['guess']) > randomNum:
        return("Too High, Try Again!")
    else:
        return("Yay, you won!!")
    return redirect('/')

@app.route('/')
def resetting():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)


     # if 'c' not in session:
    #     session['count'] = 0