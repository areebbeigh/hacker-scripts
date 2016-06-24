# Author: Areeb Beigh
# Created: 10th April 2016

''' 
Description: Makes a temporary playlist of the music files in the folder in 
config.ini [hs-music] and opens it with the default media player  
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

# Gets the music directory from config.ini
directory = Config.get("hs-music", "directory")

def main():
	execute()

def execute():
	# If the directory has been specified in config.ini then ...
	if (directory != ""):
		# Gets a list of the files in the specified directory
		files = os.listdir(directory)
		
		# Variable to store the file count in the directory
		fileCount = 0

		print("{0} Playing {1}".format(whiteSpace, directory))

		# Creates a temporary playlist
		playlist = open('playlist.m3u', 'w')
		playlist.truncate()

		for file in files:
			# If the file has a .mp3 extension then ...
			if (file.endswith('.mp3') or file.endswith(".MP3")):

				# Writes the file path to the temporary playlist.m3u
				playlist.write(directory + '\\' + file + '\n')
				fileCount += 1
		
		# Print the number of mp3 files added to playlist.m3u
		print("{0} {1} mp3 files detected".format(whiteSpace, fileCount))
		playlist.close()

		# Opens the file with the default media player
		os.startfile('playlist.m3u')
		os.startfile('bin\delete_playlist.py')

	# If the directory is not specified in config.ini then ...
	else:
		print("{0} Directory not specified in the config file".format(whiteSpace))

if __name__ == "__main__":
	main()