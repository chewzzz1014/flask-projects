from flask import Flask
from flask import request
# request is a global object Flask uses to put the correct incoming request data in it
# an instance of built-in Request


# create application
app = Flask("main")

# perform task depends on request we accept
# Flask route only asnwers to GET by default
@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "GET":
        template = """
        <form method = "POST">
        <input type = "text" placeholder="Username...">
        <input type = "password" placeholder="Password...">
        <input type="submit" value = "Auth">
        </form>
        """
        return template 

    elif request.method == "POST":
        return "Wow! Great, you logged in!"


'''

# query parameter (followed after ? in request URL)
@app.route("/users")
def users():
    # quert parameterd are returned in form of dict
    query_params = request.args

    city = query_params.get("city")
    age = query_params.get("age")

    result = ..do something

    return result
'''

app.run()
