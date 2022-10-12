from flask import Flask, render_template, url_for

# __name__ is directory name
app = Flask(__name__)

posts = [
    {
        "author": "chewzzz",
        "title": "First Day in School!",
        "content": "Hoorayyyyy",
        "date_post": "October 12 2022"
    },
    {
        "author": "screwdriver",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_post": "October 14 2022"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    # run in debug mode (we can see changes after refresh w/o restart flask server)
    app.run(debug=True)
