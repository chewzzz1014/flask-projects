from flask import Flask
from flask import jsonify

app = Flask("main")

# create response with jsonify to return a json
@app.route("/")
def no_data():
    response = jsonify({"message": "Haloooooooooo", "info": "Make response with jsonify", "status": 200})
    return response

app.run()