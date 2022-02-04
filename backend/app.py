from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/', methods = ['Get'])
def get_articles():
	return jsonify({"Hello":"World"})




if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)