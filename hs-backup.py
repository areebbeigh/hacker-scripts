# Author: Areeb Beigh
# Created: 28th July 2016

"""
Automatically creates a backup of all the files in the backup location. Both,
the files and the backup location are specified in the configuration
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


def isValidConfig(purge, retries, backupLocation, files):
    """ Takes all options in the "hs-backup" section as parameters and returns
    True if they are valid, else raises a ConfigError """

    try:
        purge = int(purge)
        if not (purge == 0 or purge == 1):
            raise ValueError
    except ValueError:
        raise ConfigError("Value of purge must be either 0 or 1")

    try:
        retries = int(retries)
        if not (retries > 0):
            raise ValueError
    except ValueError:
        raise ConfigError("Value of retries must be an integer greater than 0")

    if not os.path.isdir(backupLocation):
        raise ConfigError("Value of backup_location must be a valid directory)")

    for file in files:
        if not os.path.isdir(file):
            raise ConfigError("{} is not a directory".format(file))

    return True


def execute():
    purge, retries, backupLocation, directories = configReader.readConfig("hs-backup")
    logFile = "backup_log.txt"
    maxLogSize = 1 * 1024 * 1024  # Default 1 MB

    if isValidConfig(purge, retries, backupLocation, directories):
        purge = int(purge)
        retries = int(retries)

        for file in directories:
            backup = os.path.join(backupLocation, os.path.basename(file))
            if not os.path.exists(backup):
                os.makedirs(backup)

            src = file
            dst = backup
            print(whiteSpace + file, backup, sep=" -> ")
            # Removes the log file if it gets larger than maxLogSize (default 1 MB)
            try:
                if os.path.getsize(logFile) > maxLogSize:
                    os.remove(logFile)
            except FileNotFoundError:
                pass

            if purge == 0:
                command = "ROBOCOPY /LOG+:\"{0}\" /V /E /R:{1} {2} {3}".format(
                    logFile,
                    retries,
                    src,
                    dst)
            elif purge == 1:
                command = "ROBOCOPY /LOG+:\"{0}\" /V /E /PURGE /R:{1} {2} {3}".format(
                    logFile,
                    retries,
                    src,
                    dst)

            os.system(command)


if __name__ == "__main__":
    main()
