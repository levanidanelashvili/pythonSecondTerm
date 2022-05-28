from flask import Flask

app = Flask(__name__)


@app.route('/<home>')
def hello_world(home):
    return 'Hello ' + home


@app.route('/')
def hey():
    return '123'


if __name__ == '__main__':
    app.run(debug=True)
