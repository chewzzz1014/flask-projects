from flask import Flask, render_template, request
import sys
import requests


app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    api_id = "4292d2f8313dc5e93323d8dc21ae22eb"

    if request.method == 'POST':
        city = request.form['city_name']
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_id}&units=metric')
        weather_info = r.json()

        if weather_info['cod'] == 200:
            return render_template('index.html', weather=weather_info)

    return render_template('index.html')


# don't change the following way to run flask:
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
