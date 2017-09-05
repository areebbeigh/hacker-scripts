# Author: Areeb Beigh
# Created: 5th September 2017

"""
Creates a playlist of all the MP4 files in the directory and starts it.
Wrote this one because I watch a lot of anime (downloaded).
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
from src import filetools

playlist = os.path.join(os.getcwd(), "playlist.m3u")

with open(playlist, "w") as f:
    for file in filetools.natural_sort(os.listdir()):
        print(file)
        if file.lower().endswith(".mp4"):
            f.write(os.path.join(os.getcwd(), file) + "\n")

os.startfile(playlist)
