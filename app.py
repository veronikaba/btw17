from flask import Flask

app = Flask(__name__)


@app.route('/')
def say_hello():
    return'<h1>Hello</h1>'


app.run(debug=True)
