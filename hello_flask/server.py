from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/userinfo', methods=['POST'])
def userinfo():
    print("Got Post Info")
    name = request.form['name']
    location = request.form['location']
    language = request.form['language']
    # return redirect('/')
    return render_template("userinfo.html", name = name, location = location, language = language)
    
if __name__=="__main__":
    app.run(debug=True) 

