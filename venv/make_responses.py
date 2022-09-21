from flask import Flask
# instace of Response class
# allows us to:
#  set up special properties such as adding headers to an ordinary web page (or rather to the response that returns it)
# specify the language that is used for the web page, 
# list the allowed methods, like POST, PUT, GET, and many more.
from flask import make_response

app = Flask("main")


# main page
@app.route("/")
def index():
    response = make_response("<h1>The Main Page Hohoho</h1>")
    return response 

# error page
@app.route("/data/get_error/")
def return_error():
    # 400 status code
    response = make_response("<p>Opps..Sounds like an error!</p>", 400)
    return response 


app.run()

