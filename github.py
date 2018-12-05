from flask import Flask,render_template,request
import requests

app = Flask(__name__)
base_url = "https://api.github.com/users/"
@app.route("/", methods = ["GET","POST"] )

def index():
	if request.method == "POST":
		githubname = request.form.get("githubname")
		response = request.get(base_url + githubname)
		user_info = response.json()
		return render_template("index.html" , profile = user_info)

<<<<<<< HEAD
	else:
=======
	else
>>>>>>> ea0d10c7904e0ef75b142d8802178a9cb16cc077
		return render_template("index.html")
		#return "Hello, World"

if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0')
