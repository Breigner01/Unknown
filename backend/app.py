from flask import Flask, request
import Sms as Sms_api
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/", methods=['POST', "GET"])
def home():
    # t = Sms_api.Sms()
    # t.sendSMS("Hello Guys")
    return "Hello World"


@app.route("/sms", methods=['POST', 'GET'])
def incoming_sms():
    t = Sms_api.Sms()
    body = request.values.get('Body', None)
    resp = MessagingResponse()
    if "checkPassword" in body:
        t.check_password_sms(body)
    elif "generatePassword" in body:
        t.generate_password_sms(body)
    else:
        t.message("Invalid Command")
    resp.message(t.message)
    return str(resp)


if __name__ == "__main__":
    app.debug = True
    app.run()
