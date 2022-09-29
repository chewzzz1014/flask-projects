from flask import Flask, flash, redirect, get_flashed_messages, render_template

app = Flask('main')
app.config['SECRET_KEY'] = 'So-Seckrekt'


@app.route('/')
def main_view():
    flash('You hang on our site for more than 5 hours in a row. Take a break, please.', 'info')
    return render_template('main.html')


app.run()
