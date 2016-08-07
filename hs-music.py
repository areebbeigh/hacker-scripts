# Author: Areeb Beigh
# Created: 10th April 2016

"""
Makes a temporary playlist of the music files in the directories in config.ini
[hs-music] and opens it with the default media player
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

# Gets a list of all the music files in the directories and
# their sub-directories in the configuration file
music_files = config_reader.read_config("hs-music")


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
    if music_files:
        # Playlist path
        playlist = os.path.join(initializer.BASE_DIRECTORY, 'playlist.m3u')

        with open(playlist, 'w') as f:
            for file in music_files:
                f.write(file + '\n')

        print("{0} Playing {1} music files".format(white_space, len(music_files)))

        os.startfile(playlist)

        # Starts the delete_playlist script to delete the temporary playlist
        command = "START \"DELETE_PLAYLIST\" /MIN python {}".format(
            os.path.join(initializer.BASE_DIRECTORY, "delete_playlist.py"))
        os.system(command)
    else:
        raise ConfigError("No music files found in given directories")


if __name__ == "__main__":
    main()
