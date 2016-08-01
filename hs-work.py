# Author: Areeb Beigh
# Created: 10th April 2016

"""
Opens all the project files in config.ini [hs-work] with  the text editor
specified in config.ini
"""

import argparse
import os
import sys

from src import help
from src import initialize
from src.errors import *

initialize.initialize()

Config = initialize.Config
whiteSpace = initialize.whiteSpace

files = []  # Files list
editor = ""  # Text editor

# Appends all file paths from the config.ini [hs-work] section to 
# 'files' and the editor path to 'editor'
for option in Config.options("hs-work"):
    value = Config.get("hs-work", option)

    if option != "editor" and value:
        files.append(value)

    # If the variable 'editor' is already set then we wont overwrite it
    # This may occur if the user tries to specify more the one editors
    elif not editor:
        editor += value


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--help',
                        '-help',
                        action='store_true')

    args = parser.parse_args()

    if args.help:
        cmd = sys.argv[0].partition(".")[0]
        help.displayHelp(cmd)
        return

    execute()


def execute():
    # If at least one file is specified in config.ini then ...
    if len(files) > 0:
        for file in files:
            print("{0} Opening {1}".format(whiteSpace, file))
            os.system('START "" "{0}" "{1}"'.format(editor, file))

    # If no files are specified in config.ini
    else:
        raise ConfigError("No files specified in the configuration file")


if __name__ == "__main__":
    main()
