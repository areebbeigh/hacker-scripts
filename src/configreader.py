# Author: Areeb Beigh
# Created: 5th August 2016

"""
Module to read the configuration of different hacker-scripts from the
given configuration file and return the results
"""

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
        "hs-backup":     "_read_backup",
        "hs-browse":     "_read_browse",
        "hs-manage":     "_read_manage",
        "hs-music":      "_read_music",
        "hs-start":      "_read_start",
        "hs-wallpaper":  "_read_wallpaper",
        "hs-work":       "_read_work",
    }

    def __init__(self, configFile):
        """
        Creates a ConfigParser object and reads the given configuration file

        Parameters:
            configFile:
                The configuration file.
        """

        # Switches to hacker-scripts base directory
        initializer.change_to_base_dir()
        # Loads the configuration file
        self.Config = configparser.ConfigParser()
        self.Config.read(configFile)

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

    def _read_backup(self, Config):
        """
        Reads hs-backup configuration and returns a tuple of
        configuration values
        """

        purge = Config.get("hs-backup", "purge")
        retries = Config.get("hs-backup", "retries")
        backup_location = Config.get("hs-backup", "backup_location")
        directories = []

        for option in Config.options("hs-backup"):
            value = Config.get("hs-backup", option)
            if option[0:9] == "directory" and value:
                directories.append(value)

        return purge, retries, backup_location, directories

    def _read_browse(self, Config):
        """
        Reads hs-browse configuration and returns a list of
        urls
        """

        urls = []

        for option in Config.options("hs-browse"):
            url = Config.get("hs-browse", option)
            if url:
                urls.append(url)

        return urls

    def _read_manage(self, Config):
        """
        Reads the hs-manage configuration values and returns them
        """

        extensions = {}  # key - (option): value - (extensions tuple)
        locations = {}  # key - (option): value - (directory path)
        result = {}  # key - (extensions tuple): value - (directory path)
        extension_re = re.compile("^extension_set_(\d+)$")  # Example: extension_set_1,  extension_set_17
        location_re = re.compile("^location_(\d+)$")  # Example: location_1, location_17

        for option in Config.options("hs-manage"):
            ext_match = extension_re.search(option)
            opt_match = location_re.search(option)
            value = Config.get("hs-manage", option)

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

    def _read_music(self, Config):
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

        for option in Config.options("hs-music"):
            directory = Config.get("hs-music", option)
            if os.path.isdir(directory):
                music_files.extend(get_all_files(directory, extensions))

        return music_files


    def _read_start(self, Config):
        """
        Reads hs-start configuration and returns a list of programs/files
        in it
        """

        files = []

        for option in Config.options("hs-start"):
            if Config.get("hs-start", option):
                files.append(Config.get("hs-start", option))

        return files

    def _read_wallpaper(self, Config):
        """
        Reads hs-wallpaper configuration and returns a list of directories
        in it
        """

        extensions = [".png", ".jpg"]
        wallpapers = []

        for option in Config.options("hs-wallpaper"):
            directory = Config.get("hs-wallpaper", option)
            if os.path.isdir(directory):
                wallpapers.extend(get_all_files(directory, extensions))

        return wallpapers

    def _read_work(self, Config):
        """
        Reads the hs-work configuration and returns a list of files and
        the text editor to open them with
        """

        files = []
        editor = ""

        for option in Config.options("hs-work"):
            value = Config.get("hs-work", option)
            if option != "editor" and value:
                files.append(value)
            elif option == "editor":
                editor = value

        return files, editor