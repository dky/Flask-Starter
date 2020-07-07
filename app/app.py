import flask


app = flask.Flask(__name__)


@app.route('/')
def index():
    test_packages = ['test1', 'test2', 'test3']
    return flask.render_template('index.html', packages=test_packages)


if __name__ == '__main__':
    app.run(debug=True)
