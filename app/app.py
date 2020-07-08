import flask


app = flask.Flask(__name__)


def get_latest_packages():
    return [
        {'name': 'CatDog', 'version':  '1.2.3'},
        {'name': 'CatDog', 'version':  '2.3.4'},
        {'name': 'CatDog', 'version':  '5.4.4'},
    ]


@app.route('/')
def index():
    test_packages = get_latest_packages()
    return flask.render_template('index.html', packages=test_packages)


if __name__ == '__main__':
    app.run(debug=True)
