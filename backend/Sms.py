import os
from dotenv import load_dotenv
from twilio.rest import Client
from PasswordSpecifications import PasswordSpecifications
load_dotenv()


class Sms:

    def __init__(self):
        self.account_sid = os.getenv("account_sid")
        self.auth = os.getenv("auth")
        self.message = ""
        print(self.account_sid)
        print(self.auth)
        print("Twilio Initialized")

    def generate_password_sms(self, message):
        p = self.parse_message(message)
        #  call your function to generate password pass in p
        self.message = "BEN function"
        # client = Client(self.account_sid, self.auth)
        # client.messages.create(
        #     to=number,
        #     from_=os.getenv("from_number"),
        #     body=message
        # )

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

    def check_password_sms(self, message):
        pass
