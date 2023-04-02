from flask import Flask, jsonify, request
import os

app = Flask(__name__)


def helloWorld():
    return "Hello World"


@app.route('/')
def index():
    return jsonify({"Choo Choo": helloWorld()})


@app.route('/twillio')
def Send_Text():
    return "Messaging User"


@app.route('/process_location', methods=['GET', 'POST'])
def Capture_Location():
    if request.method == 'POST':
        lat = request.args.get('latitude')
        lng = request.args.get('longitude')
        return "Current Location... Lat:", lat, "\tLong:", lng
    else:
        return "Send a post please."


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
