# TODO Sensitive values like API tokens and secrets should not live in this config file.
# TODO They should be stored in something like vaultproject.io, or in environment variables.

import json
import os
import pwd
from datetime import datetime
import logging


class Config(object):

    def __init__(self,
                 app_name,
                 working_directory):

        self.version = '0.0.1'

        self.startup_time = datetime.now().timestamp()
        self.user_name = pwd.getpwuid(os.getuid())[0]
        self.app_name = app_name

        try:
            if working_directory[-1] == '/':
                working_directory = working_directory[:-1]
        except IndexError:
            pass
        self.working_directory = working_directory

        self.log_dir = '{}/logs'.format(working_directory)
        self.pid_file = '{}/pid'.format(working_directory)

        logger = logging.getLogger(self.app_name)
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        self.logger = logger

    def __repr__(self):
        return json.dumps({k: v for k, v in self.__dict__.items() if k[0] != '_'})

    def json(self):
        return {k: v for k, v in self.__dict__.items() if k[0] != '_'}