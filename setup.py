# Setup for installing hacker-scripts
import os, sys, shutil
from sys import argv

script, arguement = argv

# Gets the root directory (Drive letter for Windows)
rootDirectory = os.path.splitdrive(sys.executable)[0] + "\\"

# mainDirectory is <root directory>\hacker-scripts (Windows)
mainDirectory = os.path.join(rootDirectory, "hacker-scripts")

# binDirectory is <root directory>\hacker-scripts\bin (Windows)
scriptsDirectory = os.path.join(mainDirectory, "Scripts")

def main():
	# If the directory hacker-scripts already exists in the root directory then ...
	if (os.path.exists(mainDirectory)):
		# Asks the user whether to overrite the directory 
		print("A directory named \"hacker-scripts\" already exists in " +
		"{}, do you want to replace it? (y/N)".format(rootDirectory))

		# Changes user provided input to upper case
		choice = input().upper()

		if(choice in "Y YES".split()):
			# Removes the entire directory tree
			shutil.rmtree(mainDirectory)
			# Proceed with the installation
			install()
		else:
			sys.exit()
	
	# If hacker-scripts does not exist in the root directory then proceed with installation
	else:
		install()

def install():
	# Creates the directories hacker-scripts and hacker-scripts\bin in the root directory
	os.mkdir(mainDirectory)
	os.mkdir(scriptsDirectory)

	# Scripts to be installed are in the "scripts" directory of the downloaded package os.listdir() returns the list
	scripts = os.listdir("scripts")

	for script in scripts:
		script = os.path.join("scripts", script)

		if (not os.path.isdir(script)):
			if(script != "scripts\\hs-config.py"):
				shutil.copy(script, scriptsDirectory)
			else:
				shutil.copy(script, mainDirectory)

	# Adds C:\hacker-scripts and <root directory>\hacker-scripts\Scripts to PATH
	path = os.environ['PATH']

	if(mainDirectory not in path.split(";") or scriptsDirectory not in path.split(";")):
		os.system("setx PATH \"\"")
		os.system("setx PATH \"{};{};{}\"".format(
			path, 
			mainDirectory, 
			scriptsDirectory))

	print("""
	The installation was successful, you can use the command \"hs-help\" in a 
	new terminal to view the help documentation.
	
	Please open an new terminal session and run hs-config to configure hacker-scripts.
	If you face any problems after installation please check the documentation at 
	github.com/areeb-beigh/hacker-scripts 
	""")

if arguement == "install":
	main()
else:
	raise ValueError("Invalid arguement, pass arguement \"install\" to install hacker-scripts")