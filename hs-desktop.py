# Author: Areeb Beigh
# Created: 10th April 2016

"""
Manages your desktop by automatically placing different files to their
respective directories in config.ini [hs-desktop]
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

# Gets the path to Desktop
desktop = os.path.join(os.environ['USERPROFILE'], "Desktop")

# Paths/Directories for different file types are loaded from the
# config.ini [hs-desktop] section
paths = {
    "images": Config.get("hs-desktop", "images_directory"),
    "videos": Config.get("hs-desktop", "videos_directory"),
    "textFiles": Config.get("hs-desktop", "files_directory"),
}

# Different extension types for different file types
imageExtensions = [
    ".png",
    ".jpg",
    ".gif",
]
videoExtensions = [
    ".avi",
    ".mp4",
    ".mkv",
    ".flv",
    ".wmv",
    ".m4v",
    ".mpg",
    ".3gp",
    ".3g2",
    ".f4v"
]
textFileExtensions = [
    ".txt",
    ".ppt",
    ".doc",
    ".xls",
]


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


def execute():
    if "" not in paths.values():
        files = os.listdir(desktop)

        for file in files:
            # Creates a full path to the file in desktop
            filePath = os.path.join(desktop, file)

            if not os.path.isdir(file):
                # Splits file path and file extension
                fileName, fileExtension = os.path.splitext(filePath)

                # Further we check if the extension of the file is mentioned in
                # any of the extensions lists above and then we put the file in
                # the respective directory

                # Check for images
                if fileExtension.lower() in imageExtensions:
                    newLocation = os.path.join(paths["images"], file)

                # Check for videos
                elif fileExtension.lower() in videoExtensions:
                    newLocation = os.path.join(paths["videos"], file)

                # Check for text files
                elif fileExtension.lower() in textFileExtensions:
                    newLocation = os.path.join(paths["textFiles"], file)

                # If the file type is unknown to the program then we skip it
                else:
                    newLocation = None

                # If the file type is not unknown then ...
                if newLocation:
                    try:
                        # This moves the file to "newLocation"
                        os.rename(filePath, newLocation)
                        print("{0} Moved {1}".format(
                            whiteSpace,
                            os.path.basename(filePath)))

                    # If a file with the same name already exists then we rename
                    # the file we're operating on
                    except WindowsError:
                        fileName, fileExtension = os.path.splitext(newLocation)
                        count = 1
                        # Randomly append an integer to the end of the file name
                        while os.path.exists(newLocation):
                            newLocation = (
                                fileName +
                                " (" +
                                str(count) +
                                ")" +
                                fileExtension
                            )

                            count += 1

                        # Moves the file to "newLocation"
                        os.rename(filePath, newLocation)
                        print("{0} Renamed {1} to {2} since {1} already exists in destination folder".format(
                            whiteSpace,
                            os.path.basename(file),
                            os.path.basename(newLocation)))

    else:
        raise ConfigError("All paths are not specified in the configuration file")


if __name__ == "__main__":
    main()
