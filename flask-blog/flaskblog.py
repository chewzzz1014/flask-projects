from flask import Flask

# __name__ is directory name
app = Flask(__name__)

@app.route("/")
def hello():
    return '<h1>Hello World!</h1>'




if __name__ == "__main__":
    # run in debug mode
    app.run(debug=True)