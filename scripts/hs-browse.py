# Author: Areeb Beigh
# Created: 10th April 2016

'''
Opens all the URLs listed in config.ini [hs-browse] section
'''

import sys
import webbrowser 
import argparse
from src import help
from src import initialize

initialize.initialize()

Config = initialize.Config
whiteSpace = initialize.whiteSpace

# List of URLs to open (will be filled later)
urls = []

# Appends all URLs from the config.ini [hs-browse] section to 'urls'
for option in Config.options("hs-browse"):
	if (Config.get("hs-browse", option)):
		urls.append(Config.get("hs-browse", option))

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

	execute()

def execute():
	for url in urls:					
		print("{0} Opening {1}".format(whiteSpace, url))
		# Opens the URL with the default browser
		webbrowser.open(url)

if __name__ == "__main__":
	main()