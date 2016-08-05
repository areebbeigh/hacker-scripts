"""
This module is used to display the help content for each command
when the argument --h or --help is passed to that command
"""

import os
from src.initialize import Initialize

initializer = Initialize()

docsDir = "docs"
header = os.path.join(docsDir, "header.txt")

cmdDocs = {
    "hs-backup":    "hs-backup.txt",
    "hs-browse":    "hs-browse.txt",
    "hs-config":    "hs-config.txt",
    "hs-desktop":   "hs-desktop.txt",
    "hs-music":     "hs-music.txt",
    "hs-schedule":  "hs-schedule.txt",
    "hs-start":     "hs-start.txt",
    "hs-wallpaper": "hs-wallpaper.txt",
    "hs-work":      "hs-work.txt",
}


def display_help(cmd_name):
    """
    Displays help document for given cmd name using the "more"
    windows command, if no doc is available then prints a no help
    available message
    """

    cmd_name = os.path.basename(cmd_name)
    doc = os.path.join(docsDir, cmdDocs[cmd_name])

    if os.path.exists(doc):
        os.system("more \"{}\"".format(header))
        os.system("more \"{}\"".format(doc))
    else:
        print("No help available for", cmd_name)
