#main.py is the controller

from flask import Flask, render_template
from db import get_loners

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/display')
def display():
    loaners_ = get_loners()
    return render_template('display.html', loaners = loaners_)

if __name__ == '__main__':
    app.run(debug=True)