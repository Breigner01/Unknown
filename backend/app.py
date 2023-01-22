from flask import Flask, request, jsonify
from flask_cors import CORS
import Sms as Sms_api
import json
from twilio.twiml.messaging_response import MessagingResponse
from PasswordSpecifications.PasswordSpecifications import PasswordSpecifications
from PasswordGeneration.PasswordGenerator import PasswordGenerator
from CrackTime import CrackTime, get_strength

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['POST', "GET"])
def home():
    return "Hello World"


@app.route('/checkPassword', methods=['POST'])
def check_password():
    data = json.loads(request.data)
    password = data['password']
    strength = get_strength(password)
    time = CrackTime(password, False).show_results()
    return jsonify({"strength": strength, "time":time})

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

    password = PasswordGenerator().generate(requestData)
    time = CrackTime(password, False).show_results()
    strength = get_strength(time)
    return jsonify({"password": password, "time": time, "strength": strength})


@app.route("/test", methods=['POST'])
def test():
    data = request.data
    # length = request.form.get('length')
    print(data)
    return "Hello"


@app.route("/sms", methods=['POST', 'GET'])
def incoming_sms():
    app.logger.info("hello")
    t = Sms_api.Sms()
    body = request.values.get('Body', None)
    resp = MessagingResponse()
    if "checkPassword" in body:
        body = body.replace("checkPassword ", "")
        if "-m" in body:
            body = body.replace("-m ", "")
            t.message = t.check_password_sms(body, True)
        else:
            t.message = t.check_password_sms(body)
    elif "generatePassword" in body:
        body = body.replace("generatePassword", "")
        t.generate_password_sms(body)
    else:
        t.message = "Invalid Command"
    resp.message(t.message)
    print("goodbye")
    app.logger.info(resp.message)
    return str(resp)


if __name__ == "__main__":
    app.debug = True
    app.run()
