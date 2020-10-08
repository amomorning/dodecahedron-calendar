from flask import Flask, render_template, jsonify, send_file, request
from random import *
from flask_cors import CORS
import requests
import gen_calendar
import time
import json

app = Flask(__name__, static_folder="calendar-web\dist", template_folder="calendar-web\dist")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/random')
def random_number():
    response = {'randomNumber': randint(1, 100)}
    return jsonify(response)


@app.route('/api/calendar')
def user_calendar():
    print(request.args.get('data'))
    data = json.loads(request.args.get('data'))
    try:
        gen_calendar.year = int(data['year'][0])
        maincolor = '#' + data['maincolor']
        percolor = '#' + data['percolor']
        backcolor = '#' + data['backcolor']
        select = data['select']
        # print("new")
        # print(request.args.get('data'))
        return gen_calendar.gen_calendar(select, maincolor, percolor, backcolor)

        # return send_file('./tmp.pdf', as_attachment=True, cache_timeout=0)
    except Exception as e:
        print(e)
        return str(e)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if(app.debug):
        return requests.get('http://localhost:8080/{}'.format(path)).text
    if(len(path) > 0):
        return app.send_static_file(path)
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
