# Setup for installing hacker-scripts
import os
import sys
import shutil
import time

from sys import argv

script, arguement = argv

# Gets the root directory (Drive letter for Windows)
rootDirectory = os.path.splitdrive(sys.executable)[0] + "\\"
mainDirectory = os.path.join(rootDirectory, "hacker-scripts")
scriptsDirectory = os.path.join(mainDirectory, "scripts")

backupDirName = "hs_backup " + time.strftime("%D %H_%M_%S").replace('/', '-')
backupDir = os.path.join(rootDirectory, backupDirName)
configFile = os.path.join(mainDirectory, "config.ini")

oldConfig = ""

def main():
	global oldConfig

	if (os.path.exists(mainDirectory)):
		print("A directory named \"hacker-scripts\" already exists in " +
		"{}, do you want to replace it? (Y/N)".format(rootDirectory))

		choice = input().upper()
		affirmitive = ["Y", "YES"]

		if(choice in affirmitive):
			# Creates a backup of existing hacker-scripts directory
			# for roll back in case it is needed
			shutil.copytree(mainDirectory, backupDir)

			if(os.path.exists(configFile)):
				print("Do you want to keep your previous config file? (Y/N)")
				choice = input().upper()
				if(choice in affirmitive):
					with open(configFile, "r") as f:
						oldConfig = f.read()
			try:
				install(True)
			except Exception as e:
				rollBack(e)
		else:
			sys.exit()
	
	# If hacker-scripts does not exist in the root directory then proceed with installation
	else:
		install()

def rollBack(error):
	"""Restores previous installation of hacker-scripts if an error occurs
	while overwriting it"""

	try:
		shutil.rmtree(mainDirectory)
	except FileNotFoundError:
		pass
	finally:
		print("-------")
		print("An unexpected error occured, setup will attempt to revert changes.")
		print("You can report the issue at github.com/areeb-beigh if it is a bug.")
		print("-------")

		shutil.copytree(backupDir, mainDirectory)
		shutil.rmtree(backupDir)
		print("Changes reverted successfuly")
		print("Error that occured:")
		raise error

def install(overwrite):
	if(overwrite):
		shutil.rmtree(mainDirectory)

	shutil.copytree("scripts", scriptsDirectory)

	# Restores the old configuration file
	if(oldConfig):
		with open(configFile, "w+") as f:
			f.write(oldConfig)

	# Adds <root directory>\hacker-scripts\scripts to PATH
	path = os.environ['PATH']

	if(scriptsDirectory not in path.split(";")):
		os.system("setx PATH \"\"")
		os.system("setx PATH \"{};{}\"".format(
			path,
			scriptsDirectory))

	print("""
	The installation was successful, you can use the command \"hs-help\" in a 
	new terminal to view the help documentation.
	
	(If you saved the previous configuration you can skip this):
	Please open an new terminal session and run hs-config to configure hacker-scripts.
	If you face any problems after installation please check the documentation in
	the readme.md file or at github.com/areeb-beigh/hacker-scripts
	""")

	shutil.rmtree(backupDir)

if arguement == "install":
	main()
else:
	print("usage: setup.py install")