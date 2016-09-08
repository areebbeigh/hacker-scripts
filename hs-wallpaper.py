# Author: Areeb Beigh
# Created: 10th April 2016

"""
Chooses a random image file from the directory specified in the config.ini
[hs-wallpaper] section and sets it as the desktop background
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
import ctypes
import os
import random

# Local imports
from src.errors import *
from src.initialize import Initialize
from src.configreader import ConfigReader

initializer = Initialize()
config_file = initializer.config_file
config_reader = ConfigReader(config_file)
main = initializer.basic_main
# Gets a list of all the wallpapers in the directories (in the config file)
# and in their sub-directories as well
wallpapers = config_reader.read_config("hs-wallpaper")


def execute():
    if wallpapers:
        # Chooses a random wallpaper from the list of wallpapers
        random_wallpaper = random.choice(wallpapers)
        print(" Setting", os.path.basename(random_wallpaper), "as desktop wallpaper...")
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoW(
            SPI_SETDESKWALLPAPER,
            0,
            random_wallpaper,
            0)
    else:
        raise ConfigError("No wallpapers found in the specified directories")

if __name__ == "__main__":
    main(execute)
