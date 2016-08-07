# Author: Areeb Beigh
# Created: 11th June 2016

"""
This script creates (or overwrites) a config.ini file with the default
settings which has to be edited later, if config already exists and
overwriting is canceled it simply opens the config file in the default
application
"""

# Python imports
import argparse
import configparser
import os
import sys

# Local imports
from src import help
from src.initialize import Initialize

initializer = Initialize()
# hacker-scripts base directory
BASE_DIRECTORY = initializer.BASE_DIRECTORY
# Full path to the config file
config_file = os.path.join(BASE_DIRECTORY, initializer.config_file)
Config = configparser.ConfigParser()
Config.read(config_file)
# Default path to sublime text editor 3 on Windows
editor_path = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"

if not os.path.exists(editor_path):
    editor_path = ""


def create_file():
    """Creates a new configuration file with default values"""

    with open(config_file, "w") as f:
        f.write("; hacker-scripts configuration file\n")

        # Add sections and parameters the the config file
        Config.add_section("hs-backup")
        Config.set("hs-backup", "purge", "")
        Config.set("hs-backup", "retries", "")
        Config.set("hs-backup", "backup_location", "")
        Config.set("hs-backup", "directory1", "")
        Config.set("hs-backup", "directory2", "")
        Config.set("hs-backup", "directory3", "")

        Config.add_section("hs-browse")
        Config.set("hs-browse", "url1", "")
        Config.set("hs-browse", "url2", "")
        Config.set("hs-browse", "url3", "")

        Config.add_section("hs-desktop")
        Config.set("hs-desktop", "files_directory", "")
        Config.set("hs-desktop", "images_directory", "")
        Config.set("hs-desktop", "videos_directory", "")

        Config.add_section("hs-manage")
        Config.set("hs-manage", "extension_set_1", ".txt, .ppt, .doc, .xml")
        Config.set("hs-manage", "location_1", "")
        Config.set("hs-manage", "extension_set_2", ".jpg, .png, .gif")
        Config.set("hs-manage", "location_2", "")
        Config.set("hs-manage", "extension_set_3", ".avi, .mp4, .mkv, .flv, .wmv, .m4v, .mpg, .3gp, .3g2, .f4v")
        Config.set("hs-manage", "location_3", "")

        Config.add_section("hs-music")
        Config.set("hs-music", "directory1", "")
        Config.set("hs-music", "directory2", "")
        Config.set("hs-music", "directory3", "")

        Config.add_section("hs-start")
        Config.set("hs-start", "program1", "")
        Config.set("hs-start", "program2", "")
        Config.set("hs-start", "program3", "")

        Config.add_section("hs-wallpaper")
        Config.set("hs-wallpaper", "directory1", "")
        Config.set("hs-wallpaper", "directory2", "")
        Config.set("hs-wallpaper", "directory3", "")

        Config.add_section("hs-work")
        Config.set(
            "hs-work",
            "editor",
            editor_path)
        Config.set("hs-work", "project1", "")
        Config.set("hs-work", "project2", "")
        Config.set("hs-work", "project3", "")

        Config.write(f)

    print("Config file has been created at " + config_file)
    print("You can go ahead and configure the file.")
    os.startfile('config.ini', 'edit')
    sys.exit(0)


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

    if os.path.isfile(config_file):
        print("The file config.ini already exists, do you want to continue and " +
              "over-write the file with new settings? (y/N)")

        action = input().upper()

        if action == "Y" or action == "YES":
            create_file()
        else:
            os.startfile(config_file, 'edit')  # Opens the file for editing
            sys.exit(0)
    else:
        create_file()

main()
