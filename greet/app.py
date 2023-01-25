from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def greet():
    return "<h1>Welcome!</h1>"

@app.route('/welcome/home')
def greethome():
    return "<h1>Welcome Home!</h1>"

@app.route('/welcome/back')
def greetback():
    return "<h1>Welcome back!</h1>"
