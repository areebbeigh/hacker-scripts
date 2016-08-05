# Author: Areeb Beigh
# Created: 10th April 2016

"""
Opens all the URLs listed in config.ini [hs-browse] section
"""

import argparse
import sys
import webbrowser

from src import help
from src.initialize import Initialize
from src.configreader import ConfigReader

initializer = Initialize()
whiteSpace = initializer.whiteSpace
configFile = initializer.configFile
configReader = ConfigReader(configFile)

# List of URLs to open (will be filled later)
urls = configReader.readConfig("hs-browse")


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--help',
                        '-help',
                        action='store_true')
    args = parser.parse_args()

    if args.help:
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
