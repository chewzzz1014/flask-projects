from flask import Flask, flash, get_flashed_messages

app = Flask('main')

app.config['SECRET_KEY'] = 'So-Seckrekt'


@app.route('/')
def main_view():
    return "Hello, it's the Main Page!"


@app.route('/not_ready')
def redirect_view():
    flash('This page is not ready yet! Return later!')
    return get_flashed_messages()[0]


app.run()
