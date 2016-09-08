# Author: Areeb Beigh
# Created: 7th August 2016

"""
Manages all files that have one of a given set of extensions in a directory
by moving them to their respective correct locations (config dependent)
"""

#############################################################################
#    Copyright (C) 2016  Areeb Beigh <areebbeigh@gmail.com>                 #
#                                                                           #
#    This program is free software: you can redistribute it and/or modify   #
#    it under the terms of the GNU General Public License as published by   #
#    the Free Software Foundation, either version 3 of the License, or      #
#    (at your option) any later version.                                    #
#                                                                           #
#    This program is distributed in the hope that it will be useful,        #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#    GNU General Public License for more details.                           #
#                                                                           #
#    You should have received a copy of the GNU General Public License      #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.  #
#############################################################################

# Python imports
import argparse
import os
import sys

# Local imports
from src import help
from src.initialize import Initialize
from src.configreader import ConfigReader

initializer = Initialize()
config_file = initializer.config_file
config_reader = ConfigReader(config_file)
# Gets a Extensions-Directory key-value pair
loc_pairs = config_reader.read_config("hs-manage")


def main():
    parser = argparse.ArgumentParser(add_help=True, allow_abbrev=False)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d',
                       '--directory',
                       nargs=1,
                       metavar='DIR',
                       help='directory to manage files in')
    group.add_argument('-dh',
                       '--dhelp',
                       action='store_true',
                       help='displays detailed help for this hacker-script')

    args = parser.parse_args()

    if args.directory:
        execute(args.directory[0])
    elif args.dhelp:
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
                        print(" Renaming {0} to {1} since file already exists".format(
                            file,
                            os.path.basename(new_location)
                        ))
                # Uses windows shell command if the new location drive is different
                # from the old location drive because Python's os.rename can't move files
                # from one drive to another on windows
                if os.path.splitdrive(new_location)[0] == os.path.splitdrive(old_location)[0]:
                    os.rename(old_location, new_location)
                else:
                    print(" -> Other drive detected, using windows move command")
                    command = "move /-Y \"{0}\" \"{1}\"".format(
                        old_location,
                        new_location
                    )  # /-Y - prompt to overwrite (which shouldn't occur actually but eh)
                    os.system(command)
                print(" Moved {0} to {1}".format(
                    file,
                    new_directory
                ))


if __name__ == "__main__":
    main()
