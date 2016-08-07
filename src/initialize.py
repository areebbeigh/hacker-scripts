"""
This script is used in most of the hacker-script programs to do the initial stuff
"""

import os


class Initialize:
    """
    Holds string properties (the base directory, white space and
    the configuration file name) and methods for other imporatant
    initializations
    """

    def __init__(self):
        # Sets the base directory
        self._BASE_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # White space appended before printed statements
        self._white_space = "    "
        # The configuration file name
        self._config_file = "config.ini"

    @property
    def BASE_DIRECTORY(self):
        return self._BASE_DIRECTORY

    @property
    def white_space(self):
        return self._white_space

    @property
    def config_file(self):
        return self._config_file

    def change_to_base_dir(self):
        """ Changes the current working directory to the base directory """
        os.chdir(self.BASE_DIRECTORY)
