import json
import os

FILE_NAME = "data.json"


class Memory:

    def __init__(self):
        if not os.path.exists(FILE_NAME):
            with open(FILE_NAME, "w") as f:
                json.dump({}, f)

    def load(self):
        with open(FILE_NAME, "r") as f:
            return json.load(f)

    def save(self, data):
        with open(FILE_NAME, "w") as f:
            json.dump(data, f, indent=4)

    def set(self, key, value):
        data = self.load()
        data[key] = value
        self.save(data)

    def get(self, key):
        data = self.load()
        return data.get(key)