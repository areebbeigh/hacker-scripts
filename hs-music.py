# Author: Areeb Beigh
# Created: 10th April 2016

"""
Makes a temporary playlist of the music files in the directories in config.ini
[hs-music] and opens it with the default media player
"""

import argparse
import os
import sys

from src import help
from src import initialize
from src.errors import *

initialize.initialize()

Config = initialize.Config
whiteSpace = initialize.whiteSpace

# Gets the music directory from the config.ini [hs-music] section
directories = []

for option in Config.options("hs-music"):
    if Config.get("hs-music", option):
        directories.append(Config.get("hs-music", option))


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


def isValidExt(fileName):
    """Takes a file name (string) as an argument and checks if the file
    has valid extensions for a music file"""

    extensions = [
        ".mp3",
        ".m4a",
        ".ogg",
        ".flac"
    ]

    for extension in extensions:
        if fileName.endswith(extension) or fileName.endswith(extension.upper()):
            return True

    return False


def getMusicFiles(directory):
    """Returns a list of all the music files from a given directory and
    it's sub-directories"""

    musicFiles = []
    files = os.listdir(directory)

    for file in files:
        # Because the initialize module changes the CWD,
        # variable 'file' contain must be the full path to the file
        file = os.path.join(directory, file)
        if os.path.isdir(file):
            musicFiles.extend(getMusicFiles(file))
        elif isValidExt(file):
            musicFiles.append(file)

    return musicFiles


def execute():
    # If the directory has been specified in config.ini then ...
    if directories:
        files = []

        for directory in directories:
            files.extend(getMusicFiles(directory))

        # Variable to store the file count in the directory
        fileCount = 0

        print("{0} Playing {1}".format(whiteSpace, directory))

        # Creates a temporary playlist
        with open('playlist.m3u', 'w+') as playlist:
            for file in files:
                # Writes the file path to the temporary playlist.m3u
                playlist.write(file + '\n')
                fileCount += 1

        # Print the number of mp3 files added to playlist.m3u
        print("{0} {1} mp3 files detected".format(whiteSpace, fileCount))
        playlist.close()

        m3uFile = os.path.join(os.getcwd(), "playlist.m3u")

        # Opens the file with the default media player
        os.startfile(m3uFile)
        # delete_playlist.py deletes the temporary playlist
        os.system(
            "START \"delete_playlist.py\" /MIN python delete_playlist.py")

    # If the directory is not specified in config.ini then ...
    else:
        raise ConfigError("Music directories are not specified in the configuration file")


if __name__ == "__main__":
    main()
