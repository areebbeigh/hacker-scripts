# Author: Areeb Beigh
# Created: 10th April 2016

'''
Description: Opens all the URLs listed in config.ini [Browser] section
'''

import webbrowser, configparser, os, sys

# Gets the root directory (Drive letter in case of windows)
rootDirectory = os.path.splitdrive(sys.executable)[0]

# Changes the current working directory
os.chdir(os.path.join(rootDirectory, "\\hacker-scripts"))

# Creates an instance of ConfigParser()
Config = configparser.ConfigParser()
whiteSpace = "    "

# Reads/Loads the config.ini configuration file
Config.read("config.ini")

# List of URLs to open (will be filled later)
urls = []

# Appends all URLs from the config.ini [hs-browse] section to 'urls'
for option in Config.options("hs-browse"):
	if (Config.get("hs-browse", option)):
		urls.append(Config.get("hs-browse", option))

def main():
	execute()

def execute():
	for url in urls:					
		print("{0} Opening {1}".format(whiteSpace, url))
		# Opens the URL with the default browser
		webbrowser.open(url)

if __name__ == "__main__":
	main()