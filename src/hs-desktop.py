# Author: Areeb Beigh
# Created: 10th April 2016

'''
Description: Manages your desktop by automatically placing different
files to their respective directories in config.ini [Manage_Dekstop]
'''

import os, random, initialize

Config = initialize.Config
whiteSpace = initialize.whiteSpace

# Gets the path to Desktop
desktop = os.path.join(os.environ['USERPROFILE'], "Desktop")

# Paths/Directories for different file types are loaded from the config.ini [hs-desktop] seciton
paths = { 
	"images": Config.get("hs-desktop", "images_directory"),
	"videos": Config.get("hs-desktop", "videos_directory"),
	"textFiles": Config.get("hs-desktop", "files_directory"),
	}

# Different extension types for different file types
imageExtensions = [
		".png", 
		".jpg", 
		".gif",
		]
videoExtensions = [
		".avi", 
		".mp4", 
		".mkv", 
		".flv", 
		".wmv", 
		".m4v", 
		".mpg", 
		".3gp", 
		".3g2", 
		".f4v"
		]
textFileExtensions = [
		".txt", 
		".ppt", 
		".doc", 
		".xls",
		]

def main():
	execute()

def execute():
	# If the path values are not set then this block wont execute
	if (not("" in paths.values())):

		# Lists the files on the desktop
		files = os.listdir(desktop)
		
		for file in files:
			# Creates a full path to the file in desktop
			filePath = os.path.join(desktop, file)

			# If the file is not a directory then ...
			if not(os.path.isdir(file)):
				# Splits file path and file extension
				fileName, fileExtension = os.path.splitext(filePath)

				# Further we check if the extension of the file is mentioned in a any of the extension
				# lists above and then we put the file in the respective directory

				# Check for images
				if fileExtension.lower() in imageExtensions:
					newLocation = os.path.join(paths["images"], file)

				# Check for videos
				elif fileExtension.lower() in videoExtensions:
					newLocation = os.path.join(paths["videos"], file)

				# Check for text files
				elif fileExtension.lower() in textFileExtensions:
					newLocation = os.path.join(paths["textFiles"], file)

				# If the file type is unknown to the program then we skip it
				else:
					newLocation = None
				
				# If the file type is not unknown then ...
				if (newLocation):
					try:
						# This moves the file to "newLocation"
						os.rename(filePath, newLocation)
						print("{0} Moved {1}".format(
							whiteSpace, 
							os.path.basename(filePath)))

					# If the file already exists then we rename the file we're operating on
					except (WindowsError):
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