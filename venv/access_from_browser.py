from flask import Flask, request

app = Flask("main")

MAIN_PAGE_GET = '''
<h1>Welcome!</h1>
<form method='post'>
<input type='submit' value='Push me!'>
</form>
'''

MAIN_PAGE_POST = '''
<h1>Perfect!</h1>
<p>You succesfully sent POST request via your browser!</p>
'''


# send POST request 
# GET by default, when user click the button, sent POST request
@app.route("/", methods=["GET", "POST"])
def main_view():
    if request.method == "GET":
        return MAIN_PAGE_GET
    elif request.method == "POST":
        return MAIN_PAGE_POST



app.run()