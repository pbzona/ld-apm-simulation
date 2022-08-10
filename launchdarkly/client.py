import os
import ldclient
from ldclient.config import Config

class LDClient:
    __instance = None

    # Creating this method solely for code readability in the app.py file
    @staticmethod
    def instantiate():
        LDClient.get_instance()

    @staticmethod
    def get_instance():
        if LDClient.__instance == None:
            LDClient()
        return LDClient.__instance

    def __init__(self):
        if LDClient.__instance != None:
            raise Exception("Instance of LDClient already exists")
        # Setup client
        ld_sdk_key = os.environ.get('LD_SDK_KEY')
        ldclient.set_config(Config(ld_sdk_key))
        LDClient.__instance = ldclient.get()