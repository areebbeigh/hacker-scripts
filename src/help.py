"""
This module is used to display the help content for each command
when the argument --h or --help is passed to that command
"""

# Python imports
import os

# Local imports
from src.initialize import Initialize

initializer = Initialize()
initializer.change_to_base_dir()

docsDir = "docs"
header = os.path.join(docsDir, "header.txt")
footer = os.path.join(docsDir, "footer.txt")

cmdDocs = {
    "hs-backup":    "hs-backup.txt",
    "hs-browse":    "hs-browse.txt",
    "hs-config":    "hs-config.txt",
    "hs-desktop":   "hs-desktop.txt",
    "hs-manage":    "hs-manage.txt",
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
    doc = ''
    try:
        doc = os.path.join(docsDir, cmdDocs[cmd_name])
    except KeyError:
        print("No help available for", cmd_name)
        exit()

    if os.path.exists(doc):
        os.system("more \"{}\"".format(header))
        os.system("more \"{}\"".format(doc))
        os.system("more \"{}\"".format(footer))
    else:
        print("No help available for", cmd_name)
