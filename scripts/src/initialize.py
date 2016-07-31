'''
This script is used in most of the hacker-script programs to do the initial stuff
'''

import os
import sys
import configparser

def initialize():
	"""Initializes stuff"""

	global rootDirectory
	global Config
	global whiteSpace

	# Gets the root directory (Drive letter in case of windows)
	rootDirectory = os.path.splitdrive(sys.executable)[0]

	# Changes the current working directory
	os.chdir(os.path.join(rootDirectory, "\\hacker-scripts"))

	# Creates an instance of ConfigParser()
	Config = configparser.ConfigParser()
	whiteSpace = "    "

	# Reads/Loads the config.ini configuration file
	Config.read("config.ini")