from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flaskuser:flask@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route('/get', methods = ['Get'])
def get_articles():
	return jsonify({"Hello":"Jonas"})


db = SQLAlchemy(app)

class Articles(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100))
	title = db.Column(db.Text())
	date = db.Column(db.DateTime, default = datetime.datetime.now)

	def __init__(self, title, body):
		self.title = title 
		self.body = body

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)