from flask import Flask, request


app = Flask(__name__)


@app.route("/", methods=['POST', "GET"])
def home():
    return "Hello World"


if __name__ == "__main__":
    app.debug = True
    app.run()
