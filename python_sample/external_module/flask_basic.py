from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

# $env:FLASK_APP="flask_basic.py"
# $env:FLASK_DEBUG="True"
# flask run