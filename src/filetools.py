# Author: Areeb Beigh
# Created: 5th August 2016

"""
This module contains methods that help in working with files
and directories
"""

import os


def get_all_files(directory, extensions):
    """
    Returns a list of all the files from a directory and it's
    sub-directories with a specific extension

    Parameters:
            directory:
                The directory to scan.

            extensions:
                A list containing the file extensions
                to scan for.
                Example: [".png", ".jpg"]

     """

    files = []

    for file in os.listdir(directory):
        file = os.path.join(directory, file)
        if os.path.isdir(file):
            files.extend(get_all_files(file, extensions))
        elif os.path.splitext(file)[1].lower() in extensions:
            files.append(file)

    return files
