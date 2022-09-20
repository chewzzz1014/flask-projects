from flask import Flask
app = Flask("super-app")

@app.route("/")
def index():
	return "Hello World"

app.run()