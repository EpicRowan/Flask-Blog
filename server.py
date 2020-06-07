from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.secret_key = "Supermegasecret"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite///blog'

db = SQLAlchemy(app) 

class Blogpost(db.Model):
	id = db.Column(db.Integer, primary_key = True)

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

if __name__ == "__main__":
	app.run(debug=True, port=5000, host='0.0.0.0')