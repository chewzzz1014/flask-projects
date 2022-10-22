from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# __name__ is directory name
app = Flask(__name__)

# set secret key
app.config['SECRET_KEY'] = '3a9d3d30d839272b9401294f3cf59ebf'
# configure database link
#  link is relative path to file
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
# instance of database
db = SQLAlchemy(app)

# orm class
class User(db.Model):
    # primary key
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email= db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    # connect to Post class through author
    # lazy=True so that sqlalchemy will load data from database when necessary in one go
    posts = db.relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

# orm class
class Post(db.Model):
    # primary key
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    contents = db.Column(db.Text, nullable=False)
    # user_id is foreign key
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

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


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # flash message (one time alert)
        if form.email.data == 'admin@blog.com' and form.password.data == 'admin123':
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful", 'danger')

    return render_template("login.html", title='Login', form=form)


with app.app_context():

    print("db.create_all() ...")
    db.create_all()

    from flaskblog import User, Post
    user_1 = User(username="chewzzz", email="C@edu.com", password="password")
    db.session.add(user_1)
    user_2 = User(username="hotChilli", email="xxx@yy.com", password="password2")
    db.session.add(user_2)

    db.session.commit()

    User.query.all()

if __name__ == "__main__":
     # run in debug mode (we can see changes after refresh w/o restart flask server)
     app.run(debug=True)
