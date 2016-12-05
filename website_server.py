from Flask import Flask
app = Flask(__name__)

@app.route(“/“)
def greetinb():
	return (“Hello, my name is Lucas.\nThis assignment was hard”)

if __name__ == (__main__):
	app.run(host = “0.0.0.0”, port = 5000)
