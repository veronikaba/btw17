from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route('/')
def say_hello():
    return send_from_directory("templates", "hello.html")


app.run(debug=True)
