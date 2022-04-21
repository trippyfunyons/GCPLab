#main.py controller

from flask import Flask, redirect, request, url_for, render_template, jsonify
from db import get_songs, create


app = Flask(__name__)


@app.route('/')
def home():
	return render_template("index.html")


@app.route('/about')
def about():
	return render_template("about.html")


@app.route('/display')
def display():
	customers = get_customers()
	return render_template('display.html', customers = customers)


@app.route('/insert_form')
def insert_form():
	return render_template("insert.html")


@app.route('/add', methods=['POST'])
def add():
	create(request.form['customername'], request.form['customerstreet'], request.form['customercity'])
	return redirect(url_for('display'))


if __name__ == '__main__':
	app.run(debug=True)



