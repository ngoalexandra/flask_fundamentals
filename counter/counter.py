from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # Set a secret key for security purposes
# Routing rules and rest of server.py below
@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
        
    session['count'] = session['count'] + 1
    return render_template('counter.html')

@app.route('/addTwo')
def adds():
    session['count'] = session['count'] + 1
    print('testtest')
    return redirect('/')

@app.route('/reset')
def reset():
    session['count'] = 0
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)