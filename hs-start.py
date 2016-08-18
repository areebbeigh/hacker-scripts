# Author: Areeb Beigh
# Created: 10th April 2016

"""
Starts all the programs in config.ini [hs-start]
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
from src.errors import *
from src.initialize import Initialize
from src.configreader import ConfigReader

initializer = Initialize()
white_space = initializer.white_space
config_file = initializer.config_file
config_reader = ConfigReader(config_file)
# List of programs/files to be opened (will be filled later)
files = config_reader.read_config("hs-start")


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


def execute():
    # At least one program / file must be specified in the config
    if len(files) > 0:
        for file in files:
            if os.path.isfile(file):
                print("{0} Opening {1}".format(white_space, file))
                os.startfile(file)
            else:
                print("{0} Skipping {1} since it does not exist".format(
                    white_space, file))
    else:
        raise ConfigError("No programs / files specified in the configuration file")


if __name__ == "__main__":
    main()
