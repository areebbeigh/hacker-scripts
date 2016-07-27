# Author: Areeb Beigh
# Created: 10th April 2016

'''
Chooses a random image file from the directory specified in the config.ini 
[hs-wallpaper] section and sets it as the desktop background 
'''

import ctypes, os, random, initialize

Config = initialize.Config
whiteSpace = initialize.whiteSpace

# Gets the directory containing the wallpapers from the config.ini 
# [hs-wallpaper] seciton
wallpaperDirectory = Config.get("hs-wallpaper", "directory")

# List of wallpapers (will be filled later)
wallpapers = []

def main():
	execute()

# Iterates over the directory of wallpapers tree and gets a list of 
# the wallpapers / images
def check(givenDir=wallpaperDirectory):
	files = os.listdir(givenDir)

	for file in files:
		directory = givenDir + "\\" + file

		# Calls check() recursively on subdirectories
		if os.path.isdir(directory):
			check(directory)
		
		# If the file is an image file then ...
		elif file.endswith(".jpg") or file.endswith(".JPG") or file.endswith(".png") or file.endswith(".PNG"):
			wallpaper = directory
			wallpapers.append(wallpaper)

def execute(givenDir=wallpaperDirectory):
	# If the wallpaper directory is specified in config.ini then ...
	if (wallpaperDirectory != ""):
		check()

		# Chooses a random wallpaper from the list of wallpapers
		randomWallpaper = random.choice(wallpapers)

		print("{0} Setting {1} as random desktop wallpaper...".format(
			whiteSpace, randomWallpaper))

		SPI_SETDESKWALLPAPER = 20

		ctypes.windll.user32.SystemParametersInfoW(
			SPI_SETDESKWALLPAPER, 0, randomWallpaper , 0)

	# If the wallpaper directory is not specified in config.ini then ...
	else:
		print("{0} No directory specified in the config file".format(whiteSpace))

if __name__ == "__main__":
	main()