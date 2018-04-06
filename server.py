from flask import Flask, redirect, render_template, session, request
app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/')
def index():
	if('counter' in session):
		session['counter'] += 1
	else:
		session['counter'] = 0
	return render_template('index.html')

@app.route('/reset')
def reset():
	session['counter'] = 0
	return str(session['counter'])

@app.route('/two')
def two():
	session['counter'] += 2
	return str(session['counter'])

app.run(debug=True)