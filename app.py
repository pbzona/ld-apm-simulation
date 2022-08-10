import logging
from threading import Thread
from flask import Flask, request
from dotenv import load_dotenv
from launchdarkly.client import LDClient
from simulation.config import TRAFFIC_THREADS
from simulation.helpers import create_log_file
from simulation.ops import increase_memory_usage
from simulation.traffic import run_traffic_simulation

load_dotenv()
LDClient.instantiate()
app = Flask(__name__)

# Base route for test calls to server
@app.route("/")
def index():
    return "Hello from the LD New Relic simulation app"

# Posting a LD user context to this route increases memory usage temporarily
@app.route("/memory", methods=["POST"])
def increase_memory():
    user_context = request.json
    app.logger.info(f"Received memory request from: {user_context['key']}")
    usage = increase_memory_usage(user_context)
    return str(usage)

if __name__ == "__main__":
    log_file = 'log/example.log'
    create_log_file(log_file)
    logging.basicConfig(filename=log_file, filemode='w', level=logging.DEBUG)

    for i in range(TRAFFIC_THREADS):
        thread = Thread(target=run_traffic_simulation, args=(app,))
        app.logger.info(f"Starting thread {i} of {TRAFFIC_THREADS - 1}")
        thread.start()

    app.run(debug=True, load_dotenv=True)