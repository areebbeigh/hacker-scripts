"""
This script is used in most of the hacker-script programs to do the initial stuff
"""

import os


class Initialize:
    """
    Holds values for the base directory, white space and
    the configuration file name as attributes to be accessed by other
    scripts
    """

    def __init__(self):
        # Sets the base directory
        self._BASE_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # White space appended before printed statements
        self._white_space = "    "
        # The configuration file name
        self._config_file = "config.ini"
        # Changes the current working directory to the base directory
        os.chdir(self._BASE_DIRECTORY)

    @property
    def BASE_DIRECTORY(self):
        return self._BASE_DIRECTORY

    @property
    def white_space(self):
        return self._white_space

    @property
    def config_file(self):
        return self._config_file
