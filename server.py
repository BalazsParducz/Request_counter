from flask import Flask, render_template, request, redirect, url_for



app = Flask(__name__)


COUNTER = 0


@app.route("/")
def main_route():
    pass


@app.route("/request-counter")
def counter():
    pass

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
