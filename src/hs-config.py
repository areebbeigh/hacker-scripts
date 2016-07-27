# Author: Areeb Beigh
# Created: 11th June 2016

'''
This script creates (or overwrites) a config.ini file with the default 
settings which has to be edited later, if config already exists and 
overwriting is canceled it simply opens the config file in the default
application
'''

import os, configparser, sys

# Gets the root directory (Drive letter in case of windows)
rootDirectory = os.path.splitdrive(sys.executable)[0]

# Changes the current working directory
os.chdir(os.path.join(rootDirectory, "\\hacker-scripts"))

Config = configparser.ConfigParser()

currentDirectory = os.getcwd()
configFile = "config.ini"
filePath = os.path.join(currentDirectory, configFile)

# Default path to sublime text editor 3 on windows
editorPath = os.path.join(
	rootDirectory, "\\Program Files\\Sublime Text 3\\sublime_text.exe")

def createFile():
			"""
			Function to create a new configuration file
			"""

			with open("config.ini", "w") as configFile:

				configFile.write(
					"# You can add as many parameters as you want to CERTAIN " +
					"sections but they must be in series\n")
				
				# Add settings and parameters the the config file
				Config.add_section("hs-browse")
				Config.set("hs-browse", "url1", "")
				Config.set("hs-browse", "url2", "")
				Config.set("hs-browse", "url3", "")

				Config.add_section("hs-music")
				Config.set("hs-music", "directory1", "")
				Config.set("hs-music", "directory2", "")
				Config.set("hs-music", "directory3", "")

				Config.add_section("hs-desktop")
				Config.set("hs-desktop", "files_directory", "")
				Config.set("hs-desktop", "images_directory", "")
				Config.set("hs-desktop", "videos_directory", "")

				Config.add_section("hs-start")
				Config.set("hs-start", "program1", "")
				Config.set("hs-start", "program2", "")
				Config.set("hs-start", "program3", "")

				Config.add_section("hs-wallpaper")
				Config.set("hs-wallpaper", "directory", "")

				Config.add_section("hs-work")
				Config.set(
					"hs-work", 
					"editor", 
					editorPath)
				Config.set("hs-work", "project1", "")
				Config.set("hs-work", "project2", "")
				Config.set("hs-work", "project3", "")
				
				Config.write(configFile)

			print("Config file has been created at " + filePath)
			print("You can go ahead and configure the file.")
			
			os.startfile("C:\\hacker-scripts\\config.ini")

			sys.exit(0)

def main():
	# Checks the a config file already exists
	if (os.path.isfile(filePath)):

		print("The file config.ini already exists, do you want to continue and " +
			"over-write the file with new settings? (y/N)")

		action = input().upper()

		# Rewrites a fresh config file
		if (action == "Y" or action == "YES"):
			createFile()
		else:
			os.startfile(filePath)
			sys.exit(0)
	else:
		createFile()

main()
