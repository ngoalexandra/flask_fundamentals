from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # Set a secret key for security purposes
# Routing rules and rest of server.py below
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Notice how the key we are using to access the info corresponds with the names
    # of the inputs from our html form
    session['name'] = request.form['name']
    sessiom['email'] = request.form['email']
    return redirect('/show') # redirects back to the '/' route
@app.route('/show')
def show_user():
    return render_template('userinfo.html', name=session['name'], email=session['email'])

if __name__=="__main__":
    app.run(debug=True)