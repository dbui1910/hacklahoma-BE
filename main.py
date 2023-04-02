from flask import Flask, jsonify
import os

app = Flask(__name__)


def helloWorld():
    return "Hello World"


@app.route('/')
def index():
    return jsonify({"Choo Choo": helloWorld()})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
