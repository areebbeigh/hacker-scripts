# Author: Areeb Beigh
# Created: 10th April 2016

'''
Description: Starts all the programs in config.ini [hs-start] 
'''

import os, configparser, sys

# Gets the root directory (Drive letter in case of windows)
rootDirectory = os.path.splitdrive(sys.executable)[0]

# Changes the current working directory
os.chdir(os.path.join(rootDirectory, "\\hacker-scripts"))

# Creates an instance of ConfigParser()
Config = configparser.ConfigParser()
whiteSpace = "    "

# Reads/Loads the config.ini configuration file 
Config.read("config.ini")

# List of programs/files to be opened (will be filled later)
files = []

# Appends all program/file paths from config.ini [hs-start] to 'files'
for option in Config.options("hs-start"):
	if (Config.get("hs-start", option) != ""):
		files.append(Config.get("hs-start", option))

def main():
	execute()

def execute():
	# If at least one program/file has been specified in config.ini then ...
	if (len(files) > 0):
		for file in files:

			# If the program/file exist then ...
			if os.path.isfile(file) == True:
				print("{0} Opening {1}".format(whiteSpace, file))
				# Starts the program/file
				os.startfile(file)
			
			# If the program/file does not exist then ...
			else:
				print("{0} Skipping {1} since it does not exist".format(whiteSpace, file))
	
	# If no program/file has been specified in config.ini
	else:
		print("{0} No programs/files specified in the config file".format(whiteSpace))

if __name__ == "__main__":
	main()