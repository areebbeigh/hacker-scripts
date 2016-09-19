# Author: Areeb Beigh
# Created: 23rd June 2016

"""
Prints a brief help documentation to the terminal
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

def main():
    print("""
    Python hacker-scripts by Areeb - github.com/areebbeigh/hacker-scripts (Feel free to contribute)

    This is a collection of mini-scripts written in Python intended to make
    frequently used or random tasks such as playing music, launching programs you use
    frequently, opening the pages you browse daily etc easier just with a single command 
    through your terminal.

    ---------
    Currently available commands:

    > hs-backup         Creates a backup of all the files in the backup location, both are specified in the config
    > hs-browse         Opens the URLs in the configuration file
    > hs-config         Creates (or overwrites) a config.ini file in the hacker-scripts directory
    > hs-help           Displays this help documentation
    > hs-manage         Manages all the files in a given directory by moving those files to their respective locations
    > hs-music          Creates and plays a temporary playlist of music files in the directories in the configuration
    > hs-schedule       Creates a new windows scheduled task that executes a hacker-scripts cmd at a time in the future
    > hs-start          Launches the programs listed in the configuration
    > hs-wallpaper      Chooses and sets a random wallpaper from the wallpapers directory specified in the configuration
    > hs-work           Opens all the files specified with the text editor (both are set in the configuration)

    Most the above scripts depend on the config.ini file located in the hacker-scripts directory.
    If you don't find a config.ini file in your hacker-scripts directory run hs-config to create one.

    The help statements for each script above is just a compact version, to view the full description,
    configuration examples and usage details of a script use:

    "<command name> -dh"

    Ex: "hs-music -h" will display hs-music's help documentation.
    """)


if __name__ == "__main__":
    main()
