from flask import Flask, render_template

app = Flask(__name__)


# add configuration
# app.config.from_object("settings")
app.config.from_envvar("FLASK_CONF_VAR")


@app.route("/")
def index():
    return render_template("index.html")


app.run()
