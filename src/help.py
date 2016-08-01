"""
This module is used to display the help content for each command
when the argument --h or --help is passed to that command
"""

import os
from src import initialize

initialize.initialize()

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


def displayHelp(cmdName):
    """Displays help document for given cmd name using the "more"
    windows command, if no doc is available then prints a no help
    available message"""

    cmdName = os.path.basename(cmdName)
    doc = os.path.join(docsDir, cmdDocs[cmdName])

    if os.path.exists(doc):
        os.system("more \"{}\"".format(header))
        os.system("more \"{}\"".format(doc))
    else:
        print("No help available for", cmdName)
