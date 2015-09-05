from flask import Flask, render_template
from app import capitalData

app = Flask(__name__)

@app.route("/")
def main():
	name = capitalData.get_Name()
	return render_template('index.html', name=name)

if __name__ == "__main__":
	app.run(debug=True)