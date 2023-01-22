import os
from dotenv import load_dotenv
from twilio.rest import Client
from PasswordSpecifications.PasswordSpecifications import PasswordSpecifications
from CrackTime import CrackTime
from PasswordGeneration.PasswordGenerator import PasswordGenerator

load_dotenv()


def parse_message(message):
    special_characters = False
    numbers = False
    ambiguous = False
    lowercase = False
    uppercase = False
    min_numbers = 0
    min_symbols = 0
    length = 0

    for name in message.split(" "):
        if name == "-sc":
            special_characters = True
        elif name == "-n":
            numbers = True
        # Avoid ambiguous chars if this is set to true
        elif name == "-a":
            ambiguous = True
        elif name == "-u":
            uppercase = True
        elif name == "-l":
            lowercase = True
        elif name.isnumeric():
            length = int(name)
        else:
            pass
    return PasswordSpecifications(length=length, lowercase=lowercase, uppercase=uppercase, numbers=numbers,
                                  symbols=special_characters, min_numbers=min_numbers, min_symbols=min_symbols,
                                  ambiguous=ambiguous)


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

    def check_password_sms(self, message, use_moores=False):
        pw = CrackTime(message, use_moores)
        return pw.show_results()
