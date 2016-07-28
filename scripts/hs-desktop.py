# Author: Areeb Beigh
# Created: 28th July 2016

'''
Automatically creates a backup of all the files on the drive. Both, 
the files and the backup drive are specified in the configuration
'''

import os
from src.initialize import *

'''
purge (bool)
retries (int)
backup_drive
file1
file2
.
.
.
'''

def main():
	execute()

def isValidConfig(purge, retries, backupLocation, files):
	"""Takes all options in the "hs-backup" section as parameters and returns
	True if they are valid, else raises a ConfigError"""

	try:
		purge = int(purge)
		if(not(purge == 0 or purge == 1)):
			raise ValueError
	except ValueError:
		raise ConfigError("Value of purge must be either 0 or 1")

	try:
		retries = int(retries)
		if(not(retries > 0)):
			raise ValueError
	except ValueError:
		raise ConfigError("Value of retries must be an integer greater than 0")

	if(not os.path.isdir(backupLocation) and backupLocation != ""):
		return ConfigError("Value of backup_location must be a valid directory (available)")

	for file in files:
		if(not os.path.isdir(file)):
			raise ConfigError("{} is not a directory".format(file))

	return True

def execute():
	purge = Config.get("hs-backup", "purge")
	retries = Config.get("hs-backup", "retries")
	backupLocation = Config.get("hs-backup", "backup_location")
	directories = []

	logFile = "backup_log.txt"

	for option in Config.options("hs-backup"):
		if(option[0:9] == "directory"):
			directories.append(Config.get("hs-backup", option))

	if(isValidConfig(purge, retries, backupLocation, directories)):
		purge = int(purge)
		retries = int(retries)

		for file in directories:
			backup = os.path.join(backupLocation, os.path.basename(file))
		
			if(not os.path.exists(backup)):
				os.makedirs(backup)

			src = file
			dst = backup

			print(file, backup, sep=" -> ")

			if(purge == 0):
				command = "ROBOCOPY /LOG+:\"{0}\" /V /E /R:{1} {2} {3}".format(
					logFile,
					retries,
					src,
					dst)
			elif(purge == 1):
				command = "ROBOCOPY /LOG+:\"{0}\" /V /E /PURGE /R:{1} {2} {3}".format(
					logFile,
					retries,
					src,
					dst)

			os.system(command)
		
if(__name__ == "__main__"):
	main()