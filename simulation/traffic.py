import sys
from random import randint
from time import sleep
from simulation.config import MAX_REQ_DELAY, MIN_REQ_DELAY
from simulation.user import User

def run_traffic_simulation(app):
    while True:
        try:
            user = User(app)
            user.make_memory_request()
            sleep(randint(MIN_REQ_DELAY, MAX_REQ_DELAY))
        except KeyboardInterrupt:
            sys.exit("Exited by user")