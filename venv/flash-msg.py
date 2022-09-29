from flask import Flask, flash, get_flashed_messages

app = Flask('main')

app.config['SECRET_KEY'] = 'So-Seckrekt'


@app.route('/')
def main_view():
    return "Hello, it's the Main Page!"


@app.route('/not_ready')
def redirect_view():
    flash("It's cold in the graveyard", 'info')
    flash("You don't know whos is behind you.", 'ahtung')
    flash('There is no pain', 'error')
    flash('What are you receiving', 'interest')

    return get_flashed_messages()[2]


app.run()
