# Author: Areeb Beigh
# Created: 10th April 2016

"""
Makes a temporary playlist of the music files in the directories in config.ini
[hs-music] and opens it with the default media player
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
import os

# Local imports
from src.errors import *
from src.initialize import Initialize
from src.configreader import ConfigReader

initializer = Initialize()
config_file = initializer.config_file
config_reader = ConfigReader(config_file)
main = initializer.basic_main

# Gets a list of all the music files in the directories and
# their sub-directories in the configuration file
music_files = config_reader.read_config("hs-music")


def execute():
    if music_files:
        # Playlist path
        playlist = os.path.join(initializer.BASE_DIRECTORY, 'playlist.m3u')

        with open(playlist, 'w') as f:
            for file in music_files:
                f.write(file + '\n')

        print(" Playing", str(len(music_files)), "music files")

        os.startfile(playlist)

        # Starts the delete_playlist script to delete the temporary playlist
        command = "START \"DELETE_PLAYLIST\" /MIN python {}".format(
            os.path.join(initializer.BASE_DIRECTORY, "delete_playlist.py"))
        os.system(command)
    else:
        raise ConfigError("No music files found in given directories")

if __name__ == "__main__":
    main(execute)
