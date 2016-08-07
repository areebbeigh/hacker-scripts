# Author: Areeb Beigh
# Created: 10th April 2016

"""
Chooses a random image file from the directory specified in the config.ini
[hs-wallpaper] section and sets it as the desktop background
"""

# Python imports
import argparse
import ctypes
import os
import random
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
# Gets a list of all the wallpapers in the directories (in the config file)
# and in their sub-directories as well
wallpapers = config_reader.read_config("hs-wallpaper")


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
    if wallpapers:
        # Chooses a random wallpaper from the list of wallpapers
        random_wallpaper = random.choice(wallpapers)

        print("{0} Setting {1} as random desktop wallpaper...".format(
            white_space,
            os.path.basename(random_wallpaper)))

        SPI_SETDESKWALLPAPER = 20

        ctypes.windll.user32.SystemParametersInfoW(
            SPI_SETDESKWALLPAPER,
            0,
            random_wallpaper,
            0)
    else:
        raise ConfigError("No wallpapers found in the specified directories")


if __name__ == "__main__":
    main()
