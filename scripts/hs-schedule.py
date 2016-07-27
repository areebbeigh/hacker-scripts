# Author: Areeb Beigh
# Created: 23rd July 2016

'''
This script creates a new windows scheduled task that executes a hacker-scripts 
COMMAND script at a time in the future specified by the user

Command used: SCHTASKS
'''

import os
import time

from initialize import *

def main():
	execute()

def getCurrentTime():
	"""Returns the current time in 24 hr format as a list
	Hours at index 0 and minutes at index 1"""

	return time.strftime("%H:%M").split(":")

def isValidTime(givenTime):
	"""Given a list time this function checks if the given time is 
	in the future"""
	
	currentTime = getCurrentTime()

	givenHour = int(givenTime[0])
	givenMinute = int(givenTime[1])

	currentHour = int(currentTime[0])
	currentMinute = int(currentTime[1])

	if (givenHour <= 24 and givenMinute <= 59):
		return (
			(givenHour > currentHour) or
			(givenHour == currentHour and givenMinute > currentMinute)
			)
	
	return False

def execute():
	"""Takes all the information about the task to be scheduled and
	creates the scheduled task"""

	commands = []

	# List of ALL the files present in the bin directory
	scripts = os.listdir(os.path.join(os.getcwd(), "Scripts"))

	for script in scripts:
		# Appends all the script names that have "hs-" prefix and ".py" extension
		# to commands after removing the extension from the script name

		if(script[0:3] == "hs-" and script.endswith(".py")):
			cmdName = script.partition(".")[0]
			commands.append(cmdName)
	
	givenCmd = input("\n{}Command Name: ".format(whiteSpace))
	execTime = ""

	if(givenCmd in commands):
		while True:
			execTime_ = input("{}Execution Time (ex: 18:51): ".format(whiteSpace))
			
			if(isValidTime(execTime_.split(":"))):
				execTime += execTime_
				break
			else:
				print("{}Invalid time, the time must be in the future today".format(whiteSpace))

	else:
		raise ValueError("{} does not exist in hacker-scripts commands".format(givenCmd))

	execCmd = os.path.join(os.getcwd(), "Scripts", givenCmd + ".py")
	execName = "[{0}]_hacker-scripts_{1}".format(execTime.replace(":", "_"), givenCmd)

	print()

	# Creates a new scheduled task
	os.system("SCHTASKS /Create /SC ONCE /ST {0} /TR \"python '{1}'\" /TN {2}".format(
		execTime, execCmd, execName))

if(__name__ == "__main__"):
	main()