# Author: Areeb Beigh
# Created: 10th April 2016

'''
Description: Opens all the project files in config.ini [hs-work] with 
Sublime Text Editor (default path)
'''

import os, configparser, sys

# Gets the root directory (Drive letter in case of windows)
rootDirectory = os.path.splitdrive(sys.executable)[0]

# Changes the current working directory
os.chdir(os.path.join(rootDirectory, "\\hacker-scripts"))

# Creates an instanec of ConfigParser()
Config = configparser.ConfigParser()

# Reads/Loads the config.ini configuration file
Config.read("config.ini")
whiteSpace = "    "

files = []		# Files list
editor = ""		# Text editor

# Appends all file paths from the config.ini [hs-work] section to 'files' and the editor path to 'editor'
for option in Config.options("hs-work"):
	value = Config.get("hs-work", option)

	if (option != "editor" and value):
		files.append(value)

	# If the variable 'editor' is already set then we wont overwrite it
	# This may occur if the user tries to specify more the one editors
	elif (not editor):
		editor += value

def main():
	execute()

def execute(files=files):
	# If at least one file is specified in config.ini then ...
	if (len(files) > 0):
		for file in files:
			os.system('START "" "{0}" "{1}"'.format(editor, file))
	
	# If no files are specified in config.ini
	else:
		print("{0} No directory(ies) / file(s) specified in the config file".format(whiteSpace))

if __name__ == "__main__":
	main()