"""
This module is used to display the help content for each command
when the argument --h or --help is passed to that command
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

# Python imports
import os

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Base directory
docs_dir = "docs"
header = os.path.join(docs_dir, "header.txt")
footer = os.path.join(docs_dir, "footer.txt")
arg_tip = os.path.join(docs_dir, "tip1.txt")  # Tip for cmds that require arguments

cmd_docs = {
    "hs-backup": "hs-backup.txt",
    "hs-browse": "hs-browse.txt",
    "hs-config": "hs-config.txt",
    "hs-desktop": "hs-desktop.txt",
    "hs-manage": "hs-manage.txt",
    "hs-music": "hs-music.txt",
    "hs-schedule": "hs-schedule.txt",
    "hs-start": "hs-start.txt",
    "hs-wallpaper": "hs-wallpaper.txt",
    "hs-work": "hs-work.txt",
}

arg_cmds = ["hs-backup", "hs-manage", "hs-schedule"]  # CMDs that require arguments


def more(file_name):
    """
    Displays the text in the given file name on the terminal using the "more"
    terminal command.
    """

    os.system("more \"{}\"".format(file_name))


def display_help(cmd_name):
    """
    Displays help document for given cmd name.
    """

    cmd_name = os.path.basename(cmd_name)
    doc = ''
    try:
        doc = os.path.join(docs_dir, cmd_docs[cmd_name])
    except KeyError:
        print("No help available for", cmd_name)
        exit()

    if os.path.exists(doc):
        more(header)
        more(doc)
        if cmd_name in arg_cmds:
            more(arg_tip)
        more(footer)
    else:
        print("No help available for", cmd_name)
