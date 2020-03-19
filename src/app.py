from flask import Flask, jsonify
# This means from library import class

# __name__ references app.py
app = Flask(__name__)


@app.route('/', defaults={'name': 'Default'})
@app.route('/<name>')
def index(name):
    return '<h1>Hello {}!</h1>'.format(name)


@app.route('/home', methods=['POST'])
def home():
    return '<h1>You are on the home page</h1>'


@app.route('/json')
def json():
    return jsonify({'key': 'value1', 'key2': [1, 2, 3, 4]})


if __name__ == '__main__':
    app.run(debug=True)
