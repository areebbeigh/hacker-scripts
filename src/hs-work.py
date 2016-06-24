# Author: Areeb Beigh
# Created: 10th April 2016

'''
Description: Opens all the project files in config.ini [hs-work] with 
Microsoft Visual Studio Code (code must be in PATH)
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

# List of files to open (will be filled later)
files = []

# Appends all file paths from config.ini [hs-work] to 'files'
for option in Config.options("hs-work"):
	if (Config.get("hs-work", option) != ""):
		files.append(Config.get("hs-work", option))

def main():
	execute()

def execute(files=files):
	# If at least one file is specified in config.ini then ...
	if (len(files) > 0):
		for file in files:
			# Code is the PATH name for Microsoft Visual Code
			os.system("code " + file)
	
	# If no files are specified in config.ini
	else:
		print("{0} No directorie(s) / file(s) specified in the config file".format(whiteSpace))

if __name__ == "__main__":
	main()