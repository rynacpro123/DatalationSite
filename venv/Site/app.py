from flask import Flask, render_template, request, flash

flask_app = Flask(__name__)
flask_app.secret_key = "Man_Bear_Pig"

@flask_app.route("/hello")
@flask_app.route("/")
def index():
	return render_template("index.html")

@flask_app.route("/greet", methods=['POST', 'GET'])
def greeter():
	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	return render_template("index.html")




#start the flask app
if __name__ == "__main__":
    flask_app.run(debug=True, host="0.0.0.0", port=8000)