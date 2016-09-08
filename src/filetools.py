"""
This module contains methods that help in working with files
and directories
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

import os


def get_all_files(directory, extensions):
    """
    Returns a list of all the files from a directory and it's sub-directories with one of the given extensions.
    The sentence case of the extensions do not matter.

    Parameters:
            directory:
                The directory to scan.

            extensions:
                A list containing the file extensions
                to scan for.
                Example: [".png", ".jpg"]
     """

    extensions = [extension.lower() for extension in extensions]
    files = []

    for base, dirs, walk_files in os.walk(directory):
        for file in walk_files:
            if os.path.splitext(file)[1].lower() in extensions:
                files.append(os.path.join(base, file))

    return files
