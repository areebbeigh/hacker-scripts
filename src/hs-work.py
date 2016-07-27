# Author: Areeb Beigh
# Created: 10th April 2016

'''
Opens all the project files in config.ini [hs-work] with  the text editor 
specified in config.ini
'''

import os, initialize

Config = initialize.Config
whiteSpace = initialize.whiteSpace

# Reads/Loads the config.ini configuration file
Config.read("config.ini")
whiteSpace = "    "

files = []		# Files list
editor = ""		# Text editor

# Appends all file paths from the config.ini [hs-work] section to 
# 'files' and the editor path to 'editor'
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