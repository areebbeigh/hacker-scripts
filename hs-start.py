# Author: Areeb Beigh
# Created: 10th April 2016

"""
Starts all the programs in config.ini [hs-start]
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

# List of programs/files to be opened (will be filled later)
files = []

# Appends all program/file paths from the config.ini [hs-start] 
# section to 'files'
for option in Config.options("hs-start"):
    if Config.get("hs-start", option) != "":
        files.append(Config.get("hs-start", option))


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
    # At least one program / file must be specified in the config
    if len(files) > 0:

        for file in files:
            if os.path.isfile(file):
                print("{0} Opening {1}".format(whiteSpace, file))
                os.startfile(file)
            else:
                print("{0} Skipping {1} since it does not exist".format(
                    whiteSpace, file))
    else:
        raise ConfigError("No programs / files specified in the configuration file")


if __name__ == "__main__":
    main()
