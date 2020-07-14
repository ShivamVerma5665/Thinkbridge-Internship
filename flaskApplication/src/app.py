from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/hello')
def hello():
    return "Hello World!"

