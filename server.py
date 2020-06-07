from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.secret_key = "Supermegasecret"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app) 

class Blogpost(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(50))
	subtitle = db.Column(db.String(50))
	author = db.Column(db.String(50))
	date = db.Column(db.DateTime)
	content = db.Column(db.Text)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/post')
def post():
	return render_template('post.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/add')
def add():
	return render_template('add.html')
	
if __name__ == "__main__":
	app.run(debug=True, port=5000, host='0.0.0.0')