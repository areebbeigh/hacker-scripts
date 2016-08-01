"""
This script is used in most of the hacker-script programs to do the initial stuff
"""

import configparser
import os


def initialize():
    """Initializes stuff"""

    global Config
    global whiteSpace

    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Creates an instance of ConfigParser()
    Config = configparser.ConfigParser()
    whiteSpace = "    "

    # Reads/Loads the config.ini configuration file
    Config.read("config.ini")
