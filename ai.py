import random
import datetime


class AI:

    def __init__(self):
        self.greetings = [
            "Hi!",
            "Hello!",
            "Hey!"
        ]

    def reply(self, message):

        message = message.lower().strip()

        if message in ["hi", "hello"]:
            return random.choice(self.greetings)

        if message == "time":
            return datetime.datetime.now().strftime("%H:%M:%S")

        if message == "date":
            return datetime.datetime.now().strftime("%d/%m/%Y")

        try:
            return str(eval(message))
        except:
            pass

        if "your name" in message:
            return "My name is KHALIL AI."

        if "who made you" in message:
            return "KHALIL created me."

        if "how are you" in message:
            return "I'm doing great."

        if "bye" in message:
            return "Goodbye!"

        return "I'm still learning. I can't answer that yet."