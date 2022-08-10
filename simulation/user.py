import random
import requests
import uuid
from simulation.config import STATE_NAMES

class User:
    def __init__(self, app):
        self.id = uuid.uuid4().hex
        self.state = None
        self.app = app
        self.create_context()
        self.app.logger.info("USER CREATED: " + str(self.context))

    def create_context(self):
        self.state = random.choice(STATE_NAMES)
        self.context = {
            "key" : self.id,
            "country" : "USA",
            "custom" : {
                "state" : self.state
            }
        }

    def make_memory_request(self):
        self.app.logger.debug(f"User {self.id} making a memory request...")
        r = requests.post("http://127.0.0.1:5000/memory", json=self.context)
        self.app.logger.debug(f"User {self.id}: allocated {r.text}MB")