# Author: Areeb Beigh
# Created: 10th April 2016

'''
Starts all the programs in config.ini [hs-start] 
'''

import os

from initialize import *

# List of programs/files to be opened (will be filled later)
files = []

# Appends all program/file paths from the config.ini [hs-start] 
# section to 'files'
for option in Config.options("hs-start"):
	if (Config.get("hs-start", option) != ""):
		files.append(Config.get("hs-start", option))

def main():
	execute()

def execute():
	# At least one program / file must be specified in the config
	if (len(files) > 0):
		
		for file in files:
			if os.path.isfile(file) == True:
				print("{0} Opening {1}".format(whiteSpace, file))
				os.startfile(file)
			else:
				print("{0} Skipping {1} since it does not exist".format(
					whiteSpace, file))
	else:
		print("{0} No programs/files specified in the config file".format(
			whiteSpace))

if __name__ == "__main__":
	main()