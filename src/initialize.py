"""
This script is used in most of the hacker-script programs to do the initial stuff
"""

import configparser
import os


class Initialize:
    """ This class does the initial stuff such as changing the CWD
    and creating a ConfigParser object to read the configuration
    file """

    def __init__(self):
        # Changes the current working directory to the hacker-scripts base directory
        self.BASE_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        os.chdir(self.BASE_DIRECTORY)
        # White space appended before printed statements
        self.whiteSpace = "    "
        # Creates a ConfigParser object and reads the configuration file
        self.configFile = "config.ini"

