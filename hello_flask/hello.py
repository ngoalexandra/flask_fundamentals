from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def hello_world():
    # return "Hello World!"
    # return render_template('index.html')
    return render_template("index.html", name="Jay")
if __name__=="__main__":
    app.run(debug=True)


# from flask import Flask
# app = Flask(__name__)


# print(__name__)
# @app.route('/')

# def hello_world():
#     return "Hello World!"
# if __name__=="__main__":
#         pass

# @app.route('/success')
# def success():
#   return "success"

# @app.route("/dojo")
# def dojo():
#     return("Dojo!")

# @app.route('/say/flask')
# def say_flask():
#     return "Hi Flask"

# @app.route('/say/<name>')
# def say_name(name):
#     return f"Hi {name}!"
# # type in any name after the url and it should return "Hi + name"

# @app.route('/repeat/<num>/hello')
# def repeat_hello(num):
#     for i in range (0, int(num)):
        
#         num = int(num)
#         return (int(num) *"hello ")
# # int() returns str to an integer
# @app.route('/repeat/<num>/dogs')
# def repeat_dogs(num):
#     for i in range (0, int(num)):
        
#         num = int(num)
#         return (int(num) *"dogs ")



# app.run(debug=True)

