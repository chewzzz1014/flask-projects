from flask import Flask

# __name__ is directory name
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return '<h1>Hello World!</h1>'

@app.route("/about")
def about():
    return '<h1>About!</h1>'


if __name__ == "__main__":
    # run in debug mode (we can see changes after refresh w/o restart flask server)
    app.run(debug=True)