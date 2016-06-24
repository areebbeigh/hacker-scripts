# Author: Areeb Beigh
# Created: 10th April 2016

'''
Description: Manages your desktop by automatically placing different
files to their respective directories in config.ini [Manage_Dekstop]
'''

import os, random, configparser, sys

# Gets the root directory (Drive letter in case of windows)
rootDirectory = os.path.splitdrive(sys.executable)[0]

# Changes the current working directory
os.chdir(os.path.join(rootDirectory, "\\hacker-scripts"))

# Creates an instance of ConfigParser()
Config = configparser.ConfigParser()

# Reads/Loads the config.ini configuration file
Config.read("config.ini")

# Gets the path to Desktop
desktop = os.path.join(os.environ['USERPROFILE'], "Desktop")
whiteSpace = "    "

# Paths/Directories for different file types are loaded from config.ini
paths = { "images": Config.get("hs-desktop", "Images_Directory"),
	"videos": Config.get("hs-desktop", "Videos_Directory"),
	"textFiles": Config.get("hs-desktop", "Files_Directory"),
	}

# Different extension types for different file types
imageExtensions = [".png", ".jpg", ".gif"]
videoExtensions = [
		".avi", ".mp4", ".mkv", 
		".flv", ".wmv", ".m4v", 
		".mpg", ".3gp", ".3g2", 
		".f4v"
		]
textFileExtensions = [".txt", ".ppt", ".doc", ".xls"]

def main():
	execute()

def execute():
	# If the path values are not set then this block wont execute
	if (not("" in paths.values())):

		# Lists the files on the desktop
		files = os.listdir(desktop)
		
		for file in files:
			# Prepares a full path to the file in desktop
			filePath = desktop + "\\" + file

			# If the file is not a directory then ...
			if not(os.path.isdir(file)):
				# Splits file path and file extension
				fileName, fileExtension = os.path.splitext(filePath)

				''' 
				Further we check if the extension of the file is mentioned in a any of the extension
				lists above and then we put the file in the respective directory
				'''

				# Check for images
				if fileExtension.lower() in imageExtensions:
					newLocation = paths["images"] + "\\" + file

				# Check for videos
				elif fileExtension.lower() in videoExtensions:
					newLocation = paths["videos"] + "\\" + file

				# Check for text files
				elif fileExtension.lower() in textFileExtensions:
					newLocation = paths["textFiles"] + "\\" + file

				# The file type is unknown to the program
				else:
					newLocation = None
				
				# If the file type is not unknown then ...
				if newLocation != None:
					try:
						# This moves the file to "newLocation"
						os.rename(filePath, newLocation)
						print("{0} Moved {1}".format(
							whiteSpace, 
							os.path.basename(filePath)))

					# If the file already exists then we rename the file we're operating on
					except WindowsError:
						fileName, fileExtension = os.path.splitext(newLocation)
						oldLocation = newLocation
						# Randomly append an integer to the end of the file name
						newLocation = fileName + str(random.randint(0,20)) + fileExtension
						# Moves the file to "newLocation"
						os.rename(filePath, newLocation)
						print("{0} Renamed {1} to {2} since {1} already exists in destination folder".format(
							whiteSpace,
							os.path.basename(file),
							os.path.basename(newLocation)))
	
	# If the directory is not specified in config.ini then ...
	else:
		print("{0} All paths not specified in the config file".format(whiteSpace))

if __name__ == "__main__":
	main()