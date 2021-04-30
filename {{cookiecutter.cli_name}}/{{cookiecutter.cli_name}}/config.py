import configparser
from configparser import SafeConfigParser
import os
from pprint import pprint

import logging
import logging.config

logger = logging.getLogger(__name__)

class Config():
    def __init__(self):
        pass
    def load(self, filename, env):
        #self.config = configparser.ConfigParser()
        self.config = SafeConfigParser(os.environ)
        self.config.read(filename)
        self.__dict__.update(self.config._sections[env])

        if "STATS_DB" in os.environ:
            self.mydb = os.environ["MYDB"]

parsed = Config()

def load(filename, env):
    global parsed
    logger.info(f'loading config from {filename} with env {env}...')
    parsed.load(filename, env)

