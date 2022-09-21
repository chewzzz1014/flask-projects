from flask import Flask, render_template

app = Flask(__name__)

@app.route("/hello/<user>")
def hello_name(user):
   # Flask automatically finds the HTML file in the templates folder

   arr = [2, 4, 6]
   di = {"Jan": 1, "Feb":2 , "Mar": 3}

   return render_template("welcome.html", name=user, arr=arr, di=di)

if __name__ == "__main__":
    app.run(debug=True)