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
from src.errors import *
from src.initialize import Initialize
from src.configreader import ConfigReader

initializer = Initialize()
whiteSpace = initializer.whiteSpace
configFile = initializer.configFile
configReader = ConfigReader(configFile)
# List of files and the text editor to open them with
files, editor = configReader.readConfig("hs-work")

if not editor:
    raise ConfigError("No editor specified for the files")


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
    if len(files) > 0:
        for file in files:
            print("{0} Opening {1}".format(whiteSpace, file))
            os.system('START "" "{0}" "{1}"'.format(editor, file))

    # If no files are specified in config.ini
    else:
        raise ConfigError("No files specified in the configuration file")


if __name__ == "__main__":
    main()
