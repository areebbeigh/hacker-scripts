# Author: Areeb Beigh
# Created: 10th April 2016

"""
Chooses a random image file from the directory specified in the config.ini
[hs-wallpaper] section and sets it as the desktop background
"""

import argparse
import ctypes
import os
import random
import sys

from src import help
from src.errors import *
from src.initialize import Initialize
from src.configreader import ConfigReader

initializer = Initialize()
whiteSpace = initializer.whiteSpace
configFile = initializer.configFile
configReader = ConfigReader(configFile)
# Gets a list of all the wallpapers in the directories (in the config file)
# and in their sub-directories as well
wallpapers = configReader.readConfig("hs-wallpaper")


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
    if wallpapers:
        # Chooses a random wallpaper from the list of wallpapers
        randomWallpaper = random.choice(wallpapers)

        print("{0} Setting {1} as random desktop wallpaper...".format(
            whiteSpace,
            os.path.basename(randomWallpaper)))

        SPI_SETDESKWALLPAPER = 20

        ctypes.windll.user32.SystemParametersInfoW(
            SPI_SETDESKWALLPAPER,
            0,
            randomWallpaper,
            0)
    else:
        raise ConfigError("No wallpapers found in the specified directories")


if __name__ == "__main__":
    main()
