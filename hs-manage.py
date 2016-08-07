"""
Manages all files that have one of a given set of extensions in a directory
by moving them to their respective correct locations (config dependent)
"""

# Python imports
import argparse
import os
import sys

# Local imports
from src import help
from src.errors import *
from src.initialize import Initialize
from src.configreader import ConfigReader

initializer = Initialize()
white_space = initializer.white_space
config_file = initializer.config_file
config_reader = ConfigReader(config_file)
# Gets a Directory-Extensions key-value pair
loc_pairs = config_reader.read_config("hs-manage")


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--help',
                        '-help',
                        action='store_true')
    parser.add_argument('directory',
                        nargs='?',
                        help='directory to manage files in')

    args = parser.parse_args()

    if args.directory:
        execute(args.directory)
    else:
        cmd = sys.argv[0].partition(".")[0]
        help.display_help(cmd)
        return


def execute(directory):
    if not os.path.isdir(directory):
        print("Invalid directory:", directory)
        return

    for file in os.listdir(directory):
        for extn_tuple in loc_pairs:
            if ("." + file.partition(".")[2]) in extn_tuple:
                new_directory = loc_pairs[extn_tuple]
                old_location = os.path.join(directory, file)
                new_location = os.path.join(new_directory, file)
                i = 0  # Number assigned at the end of the file if it already exists
                while os.path.exists(new_location):
                    i += 1
                    name, dummy, extension = file.partition(".")
                    _file = name + "(" + str(i) + ")" + "." + extension
                    new_location = os.path.join(new_directory, _file)
                    if not os.path.exists(new_location):
                        print("{0} Renaming {1} to {2} since file already exists".format(
                            white_space,
                            file,
                            os.path.basename(new_location)
                        ))
                # Uses windows shell command if the new location drive is different
                # from the old location drive because Python's os.rename can't move files
                # from one drive to another on windows
                if os.path.splitdrive(new_location) == os.path.splitdrive(old_location):
                    os.rename(old_location, new_location)
                else:
                    print("{} -> Other drive detected, sing windows move command".format(white_space))
                    command = "move /-Y \"{0}\" \"{1}\"".format(
                        old_location,
                        new_location
                    )  # /-Y - prompt to overwrite (which shouldn't occur actually but eh)
                    os.system(command)
                print("{0} Moved {1} to {2}".format(
                    white_space,
                    file,
                    new_directory
                ))


if __name__ == "__main__":
    main()
