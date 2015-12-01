from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	#return "<h1> Home! </h1>"
	return render_template("home.html")

@app.route('/signin', methods=['GET'])
def signin_form():
	#return '''<form action="/signin" method="post">
	#		  <p><input name="username"></p>
	#		  <p><input name="password"></p>
	#		  <p><button type="submit">Log in</button></p>
	#		  </form>'''
	return render_template("form.html")
	
@app.route('/signin', methods=['POST'])
def signin():
	#if request.form['username']=='andy' and request.form['password']=='123456':
	#	return "<h1> Hello, Andy^_^</h1>"
	#return "<h2>bad username or password</h2>"
	username = request.form["username"]
	password = request.form["password"]
	
	if username=="andy" and password=="123456":
		return render_template("signin-ok.html", username=username)
	return render_template("form.html", message="bad username or password", username=username)
	
if __name__ == "__main__":
	app.run(host="192.168.233.138", port=8083, debug=True)
