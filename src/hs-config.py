# Author: Areeb Beigh
# Created: 11th June 2016

'''
This script creates a new config.ini file with the default settings which you have to edit later
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

# Creates a new config file
def createFile():
            configFile = open(filePath, 'w')
            configFile.truncate()   # Clears the config file

            configFile.write("# You can add as many parameters as you want to CERTAIN sections but they must be in series\n")
            
            # Add settings and parameters the the config file
            Config.add_section("hs-browse")
            Config.set("hs-browse", "URL1", "")
            Config.set("hs-browse", "URL2", "")
            Config.set("hs-browse", "URL3", "")

            Config.add_section("hs-music")
            Config.set("hs-music", "directory", "")

            Config.add_section("hs-desktop")
            Config.set("hs-desktop", "Files_Directory", "")
            Config.set("hs-desktop", "Images_Directory", "")
            Config.set("hs-desktop", "Videos_Directory", "")

            Config.add_section("hs-start")
            Config.set("hs-start", "Program1", "")
            Config.set("hs-start", "Program2", "")
            Config.set("hs-start", "Program3", "")

            Config.add_section("hs-wallpaper")
            Config.set("hs-wallpaper", "directory", "")

            Config.add_section("hs-work")
            Config.set("hs-work", "Project1", "")
            Config.set("hs-work", "Project2", "")
            Config.set("hs-work", "Project3", "")
            
            Config.write(configFile)
            configFile.close()

            print("Config file has been created at " + filePath)
            print("You can go ahead and configure the file.")
            
            os.startfile("C:\\hacker-scripts\\config.ini")

            sys.exit(0)

def main():
    # Checks the a config file already exists
    if (os.path.isfile(filePath)):

        print("The file config.ini already exists, do you want to continue and over-write "
            "the file with new settings? (y/N)")

        action = input().upper()

        # Rewrites a fresh config file
        if (action == "Y" or action == "YES"):
            createFile()
        else:
            sys.exit(0)
    else:
        createFile()

main()
