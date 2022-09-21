from flask import Flask
app = Flask("super-app")

@app.route("/")
def index():
	return "Hello World: Main Page"

@app.route("/all")
@app.route("/about")
def all_about():
	return "You see me at all page or about page!"

@app.route("/staff/<name>/")
def staff(name):
	return "Staff: " + name

@app.route("/movies/<genre>/<title>/")
def movie(genre, title):
	return "There will be a " + genre+ " movie " + title + "here"

# type conversion
@app.route('/movies/type/<movies_id>/')
def render_movies(movies_id):
    print(type(movies_id))	# appear in console
    return ""

@app.route('/movies/type/<int:movies_id>/')
def render_book(movies_id):
    print(type(movies_id))	# appear in console
    return ""

app.run()