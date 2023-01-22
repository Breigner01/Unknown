import os
from dotenv import load_dotenv
from twilio.rest import Client
from PasswordSpecifications import PasswordSpecifications
from CrackTime import CrackTime
from PasswordGeneration.PasswordGenerator import PasswordGenerator

load_dotenv()


def parse_message(message):
    p = PasswordSpecifications()
    for name in message.split(" "):
        if name == "-sc":
            p.special_characters = True
        elif name == "-n":
            p.numbers = True
        # Avoid ambiguous chars if this is set to true
        elif name == "-a":
            p.ambiguous = True
        elif name == "-u":
            p.uppercase = True
        elif name == "-l":
            p.lowercase = True
        elif name.isnumeric():
            p.length = int(name)
        else:
            pass
    return p

class Sms:

    def __init__(self):
        self.account_sid = os.getenv("account_sid")
        self.auth = os.getenv("auth")
        self.message = ""
        print(self.account_sid)
        print(self.auth)
        print("Twilio Initialized")

    def generate_password_sms(self, message):
        p = parse_message(message)
        #  call your function to generate password pass in p
        pw_gen = PasswordGenerator()
        self.message = pw_gen.generate(p)
        # client = Client(self.account_sid, self.auth)
        # client.messages.create(
        #     to=number,
        #     from_=os.getenv("from_number"),
        #     body=message
        # )

    def check_password_sms(self, message, use_moores):
        pw = CrackTime(message, use_moores)
        return pw.show_results()
