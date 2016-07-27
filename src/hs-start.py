# Author: Areeb Beigh
# Created: 10th April 2016

'''
Starts all the programs in config.ini [hs-start] 
'''

import os, initialize

Config = initialize.Config
whiteSpace = initialize.whiteSpace

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
				print("{0} Skipping {1} since it does not exist".format(
					whiteSpace, file))
	
	# If no program/file has been specified in config.ini
	else:
		print("{0} No programs/files specified in the config file".format(
			whiteSpace))

if __name__ == "__main__":
	main()