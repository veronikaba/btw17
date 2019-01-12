from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def say_hello():
    return render_template('hello.html')


app.run(debug=True)
