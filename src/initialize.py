"""
This script is used in most of the hacker-script programs to do the initial stuff
"""

#################################################################################
#    Copyright (C) 2016  Areeb Beigh <areebbeigh@gmail.com>                     #
#                                                                               #
#    This library is free software; you can redistribute it and/or              #
#    modify it under the terms of the GNU Lesser General Public                 #
#    License as published by the Free Software Foundation; either               #
#    version 2.1 of the License, or (at your option) any later version.         #
#                                                                               #
#    This library is distributed in the hope that it will be useful,            #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of             #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU          #
#    Lesser General Public License for more details.                            #
#                                                                               #
#    You should have received a copy of the GNU Lesser General Public           #
#    License along with this library; if not, write to the Free Software        #
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA  #
#################################################################################

# Python imports
import argparse
import os
import sys

# Local imports
from src import help


class Initialize:
    """
    Holds string properties (the base directory, white space and
    the configuration file name) and methods for other important
    initializations
    """

    def __init__(self):
        # Sets the base directory
        self._BASE_DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # The configuration file name
        self._config_file = "config.ini"

    @property
    def BASE_DIRECTORY(self):
        return self._BASE_DIRECTORY

    @property
    def config_file(self):
        return self._config_file

    def change_to_base_dir(self):
        """ Changes the current working directory to the base directory """
        os.chdir(self.BASE_DIRECTORY)

    def basic_main(self, execute_method):
        """
        A simple form of the main() function used by most of the hacker-scripts

        Parameters:
            execute_method:
                The method to execute after finishing with the main method.
                This method is executed only if any of the help arguments are not passed while
                executing a hacker-script.
        """
        parser = argparse.ArgumentParser(add_help=True)
        parser.add_argument('-dhelp',
                            '--dhelp',
                            action='store_true',
                            help='displays detailed help for this hacker-script')
        args = parser.parse_args()

        if args.dhelp:
            cmd = sys.argv[0].partition(".")[0]
            help.display_help(cmd)
            return

        execute_method()
