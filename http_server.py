from flask import Flask

app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def hello():
    print('Hello')
    return "Hello, World!"

if __name__ == '__main__':
    app.run(port=8888, debug=True)
