from flask import Flask, render_template
<<<<<<< HEAD:runserver.py
from app import capitalData
=======
>>>>>>> 70e025d12829e20833cdb9b27402da3fed079a91:app/users/__init__.py

app = Flask(__name__)

@app.route("/")
def main():
<<<<<<< HEAD:runserver.py
	name = capitalData.get_Name()
	return render_template('index.html', name=name)
=======
	return "hello world"
@app.errorhandler(404)
def not_found(error):
        return render_template('404.html'), 404

>>>>>>> 70e025d12829e20833cdb9b27402da3fed079a91:app/users/__init__.py

    
if __name__ == "__main__":
	app.run(debug=True)
