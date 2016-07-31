# Author: Areeb Beigh
# Created: 11th June 2016

'''
This script creates (or overwrites) a config.ini file with the default 
settings which has to be edited later, if config already exists and 
overwriting is canceled it simply opens the config file in the default
application
'''

import os
import sys
import configparser
import argparse
from src import help
from src import initialize

initialize.initialize()

rootDirectory = initialize.rootDirectory
Config = initialize.Config

currentDirectory = os.getcwd()
configFile = os.path.join(currentDirectory, "config.ini")

# Default path to sublime text editor 3 on Windows
editorPath = os.path.join(
	rootDirectory, 
	"\\Program Files\\Sublime Text 3\\sublime_text.exe")

def createFile():
			"""Creates a new configuration file with default values
			"""

			with open(configFile, "w") as f:

				f.write("; hacker-scripts configuration file\n")
				
				# Add sections and parameters the the config file
				Config.add_section("hs-backup")
				Config.set("hs-backup", "purge", "")
				Config.set("hs-backup", "retries", "")
				Config.set("hs-backup", "backup_location", "")
				Config.set("hs-backup", "directory1", "")
				Config.set("hs-backup", "directory2", "")
				Config.set("hs-backup", "directory3", "")

				Config.add_section("hs-browse")
				Config.set("hs-browse", "url1", "")
				Config.set("hs-browse", "url2", "")
				Config.set("hs-browse", "url3", "")

				Config.add_section("hs-desktop")
				Config.set("hs-desktop", "files_directory", "")
				Config.set("hs-desktop", "images_directory", "")
				Config.set("hs-desktop", "videos_directory", "")

				Config.add_section("hs-music")
				Config.set("hs-music", "directory1", "")
				Config.set("hs-music", "directory2", "")
				Config.set("hs-music", "directory3", "")

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
				
				Config.write(f)

			print("Config file has been created at " + configFile)
			print("You can go ahead and configure the file.")
			
			os.startfile("C:\\hacker-scripts\\config.ini")

			sys.exit(0)

def main():
	parser = argparse.ArgumentParser(add_help=False)
	parser.add_argument('--help', 
						'-help', 
						action='store_true')

	args = parser.parse_args()

	if(args.help):
		cmd = sys.argv[0].partition(".")[0]
		help.displayHelp(cmd)
		return

	if (os.path.isfile(configFile)):
		print("The file config.ini already exists, do you want to continue and " +
			"over-write the file with new settings? (y/N)")

		action = input().upper()

		if (action == "Y" or action == "YES"):
			createFile()
		else:
			os.startfile(configFile, 'edit')	# Opens the file for editing
			sys.exit(0)
	else:
		createFile()

main()
