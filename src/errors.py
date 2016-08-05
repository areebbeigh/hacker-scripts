"""
This module contains all the error raised by hacker-scripts scripts
"""


class Error(Exception):
    """ Base class for all exceptions """
    pass


class ConfigError(Error):
    """
    Raised when invalid configuration is encountered
    the configuration file
    """

    def __init__(self, message):
        self.message = message

    def __srt__(self):
        return repr(self.message)
