from flask import Flask, request, jsonify
from flask_cors import CORS
import Sms as Sms_api
import json
from twilio.twiml.messaging_response import MessagingResponse
from PasswordSpecifications.PasswordSpecifications import PasswordSpecifications

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST', "GET"])
def home():
    # t = Sms_api.Sms()
    # t.sendSMS("Hello Guys")
    return "Hello World"


@app.route("/genPassword", methods=['POST'])
def generate_password():
    data = json.loads(request.data)

    if data['specialChars']:
        data['min_symbols'] = 1
    if data['numbers']:
        data['min_numbers'] = 1

    requestData = PasswordSpecifications(length=int(data["value"]), lowercase=bool(data["lowercase"]),
                                         uppercase=bool(data["uppercase"]), numbers=bool(data["numbers"]),
                                         symbols=bool(data["specialChars"]), min_numbers=data.get('min_numbers', 0),
                                         min_symbols=data.get("min_symbols", 0), ambiguous=bool(data["ambiguousChars"]))
    print(requestData.ambiguous)
    return jsonify({"password":"HelloWorld"})


@app.route("/test", methods=['POST'])
def test():
    data = request.data
    # length = request.form.get('length')
    print(data)
    return "Hello"


@app.route("/sms", methods=['POST', 'GET'])
def incoming_sms():
    t = Sms_api.Sms()
    body = request.values.get('Body', None)
    resp = MessagingResponse()
    if "checkPassword" in body:
        body = body.replace("checkPassword", "")
        if "-m" in body:
            body = body.replace("m", "")
            t.check_password_sms(body, True)
        else:
            t.check_password_sms(body)
    elif "generatePassword" in body:
        body = body.replace("generatePassword", "")
        t.generate_password_sms(body)
    else:
        t.message("Invalid Command")
    resp.message(t.message)
    return str(resp)


if __name__ == "__main__":
    app.debug = True
    app.run()
