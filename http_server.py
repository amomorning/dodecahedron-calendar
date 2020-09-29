from flask import Flask, render_template, jsonify, send_file
from random import *
from flask_cors import CORS
import requests
import gen_calendar
import time

app = Flask(__name__, static_folder="./dist/static", template_folder="./dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/random')
def random_number():
    response = {'randomNumber': randint(1, 100)}
    return jsonify(response)


@app.route('/api/user_calendar')
def user_calendar():
    try:
        gen_calendar.cnt = 1
        gen_calendar.year = 2020
        gen_calendar.gen_calendar()
        return send_file('./tmp.pdf', as_attachment=True, cache_timeout=0)
    except Exception as e:
        return str(e)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
