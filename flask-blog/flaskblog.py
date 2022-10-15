from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

# __name__ is directory name
app = Flask(__name__)

# set secret key
app.config['SECRET_KEY'] = '3a9d3d30d839272b9401294f3cf59ebf'

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

@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # flash message (one time alert)
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title='Login', form=form)

if __name__ == "__main__":
    # run in debug mode (we can see changes after refresh w/o restart flask server)
    app.run(debug=True)
