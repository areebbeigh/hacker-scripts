"""
Module to read the configuration of different hacker-scripts from the
given configuration file and return the results
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
import configparser
import os
import re

# Local imports
from src.filetools import get_all_files
from src.initialize import Initialize
from src.errors import *

initializer = Initialize()


class ConfigReader:
    # Read method names for each hacker-script
    readMethods = {
        "hs-backup": "_read_backup",
        "hs-browse": "_read_browse",
        "hs-manage": "_read_manage",
        "hs-music": "_read_music",
        "hs-start": "_read_start",
        "hs-wallpaper": "_read_wallpaper",
        "hs-work": "_read_work",
    }

    def __init__(self, config_file):
        """
        Creates a configparser.ConfigParser() object and reads the given
        configuration file

        Parameters:
            config_file:
                The configuration file.
        """

        # Switches to hacker-scripts base directory
        initializer.change_to_base_dir()
        # Loads the configuration file
        self.Config = configparser.ConfigParser()
        self.Config.read(config_file)

    def read_config(self, script):
        """
        Calls the appropriate read method to read the configuration
        of the given script, returns None if no method is available

        Parameters:
            script:
                The hacker-script of which the configuration is
                to be read.
                Example: "hs-music"
        """

        if script not in self.readMethods:
            return None

        return eval("self." + self.readMethods[script])(self.Config)

    def _read_backup(self, config):
        """
        Reads hs-backup configuration and returns a tuple of
        configuration values
        """

        purge = config.get("hs-backup", "purge")
        retries = config.get("hs-backup", "retries")
        backup_location = config.get("hs-backup", "backup_location")
        directories = []

        for option in config.options("hs-backup"):
            value = config.get("hs-backup", option)
            if option[0:9] == "directory" and value:
                directories.append(value)

        return purge, retries, backup_location, directories

    def _read_browse(self, config):
        """
        Reads hs-browse configuration and returns a list of
        urls
        """

        urls = []

        for option in config.options("hs-browse"):
            url = config.get("hs-browse", option)
            if url:
                urls.append(url)

        return urls

    def _read_manage(self, config):
        """
        Reads the hs-manage configuration values and returns them
        """

        extensions = {}  # key - (option): value - (extensions tuple)
        locations = {}  # key - (option): value - (directory path)
        result = {}  # key - (extensions tuple): value - (directory path)
        extension_re = re.compile("^extension_set_(\d+)$")  # Example: extension_set_1,  extension_set_17
        location_re = re.compile("^location_(\d+)$")  # Example: location_1, location_17

        for option in config.options("hs-manage"):
            ext_match = extension_re.search(option)
            opt_match = location_re.search(option)
            value = config.get("hs-manage", option)

            if ext_match:
                extensions[option] = tuple(value.replace(" ", "").split(","))
            elif opt_match:
                locations[option] = value
            else:
                raise ConfigError("Invalid option name: '{}'".format(option))

        for i in range(len(extensions)):
            i += 1
            extension_set = extensions.get("extension_set_" + str(i), None)
            location = locations.get("location_" + str(i), None)
            if extension_set and location:
                # Check if the location is a directory
                if not os.path.isdir(location):
                    raise ConfigError("Invalid directory: {}".format(location))
                # Check if the extensions are in the proper format
                for extension in extension_set:
                    if not re.search(r"^\.[\w]+$", extension):
                        raise ConfigError("Invalid extension: {}".format(extension))
                # If no error occurs then add the location-extensions pair to results
                result[tuple(extension_set)] = location
            else:
                raise ConfigError("Invalid extensions-location pair: ({0})-{1}".format(
                    extension_set,
                    location))

        return result

    def _read_music(self, config):
        """
        Reads hs-music configuration and returns a list of
        directories in it
        """

        extensions = [
            ".mp3",
            ".m4a",
            ".ogg",
            ".flac",
        ]
        music_files = []

        for option in config.options("hs-music"):
            directory = config.get("hs-music", option)
            if os.path.isdir(directory):
                music_files.extend(get_all_files(directory, extensions))

        return music_files

    def _read_start(self, config):
        """
        Reads hs-start configuration and returns a list of programs/files
        in it
        """

        files = []

        for option in config.options("hs-start"):
            if config.get("hs-start", option):
                files.append(config.get("hs-start", option))

        return files

    def _read_wallpaper(self, config):
        """
        Reads hs-wallpaper configuration and returns a list of directories
        in it
        """

        extensions = [".png", ".jpg"]
        wallpapers = []

        for option in config.options("hs-wallpaper"):
            directory = config.get("hs-wallpaper", option)
            if os.path.isdir(directory):
                wallpapers.extend(get_all_files(directory, extensions))

        return wallpapers

    def _read_work(self, config):
        """
        Reads the hs-work configuration and returns a list of files and
        the text editor to open them with
        """

        files = []
        editor = ""

        for option in config.options("hs-work"):
            value = config.get("hs-work", option)
            if option != "editor" and value:
                files.append(value)
            elif option == "editor":
                editor = value

        return files, editor
