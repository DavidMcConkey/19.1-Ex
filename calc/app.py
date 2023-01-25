# Put your app in here.
from flask import Flask, request
from operations import add,sub,mult,div

app = Flask(__name__)

@app.route('/add')
def addition():
    """Add parameters a and b"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    answer = add(a,b)

    return str(answer)

@app.route('/sub')
def subtraction():
    """Subtract parameter b from a"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    answer = sub(a,b)

    return str(answer)

@app.route('/mult')
def multiplication():
    """Multiply parameters a and b"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    answer = mult(a,b)

    return str(answer)

@app.route('/div')
def division():
    """Divide parameters a and b"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    answer = div(a,b)

    return str(answer)

ops = {
    "add":add,
    "sub":sub,
    "mult":mult,
    'div':div,
}

@app.route('/math/<op>')
def do_math(op):
    """Does specified operation on numbers selected"""
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    res = ops[op](a,b)

    return str(res)