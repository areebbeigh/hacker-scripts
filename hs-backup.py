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
white_space = initializer.white_space
config_file = initializer.config_file
config_reader = ConfigReader(config_file)


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--help',
                        '-help',
                        action='store_true')

    args = parser.parse_args()

    if args.help:
        cmd = sys.argv[0].partition(".")[0]
        help.display_help(cmd)
        return

    execute()


def is_valid_config(purge, retries, backup_location, files):
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

    if not os.path.isdir(backup_location):
        raise ConfigError("Value of backup_location must be a valid directory)")

    for file in files:
        if not os.path.isdir(file):
            raise ConfigError("{} is not a directory".format(file))

    return True


def execute():
    purge, retries, backup_location, directories = config_reader.read_config("hs-backup")
    log_file = "backup_log.txt"
    max_log_size = 1 * 1024 * 1024  # Default 1 MB

    if is_valid_config(purge, retries, backup_location, directories):
        purge = int(purge)
        retries = int(retries)

        for file in directories:
            backup = os.path.join(backup_location, os.path.basename(file))
            if not os.path.exists(backup):
                os.makedirs(backup)

            src = file
            dst = backup
            print(white_space + file, backup, sep=" -> ")
            # Removes the log file if it gets larger than max_log_size (default 1 MB)
            try:
                if os.path.getsize(log_file) > max_log_size:
                    os.remove(log_file)
            except FileNotFoundError:
                pass

            if purge == 0:
                command = "ROBOCOPY /LOG+:\"{0}\" /V /E /R:{1} {2} {3}".format(
                    log_file,
                    retries,
                    src,
                    dst)
            elif purge == 1:
                command = "ROBOCOPY /LOG+:\"{0}\" /V /E /PURGE /R:{1} {2} {3}".format(
                    log_file,
                    retries,
                    src,
                    dst)

            os.system(command)


if __name__ == "__main__":
    main()
