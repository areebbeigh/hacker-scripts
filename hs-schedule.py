# Author: Areeb Beigh
# Created: 23rd July 2016

"""
This script creates a new windows scheduled task that executes a hacker-scripts
COMMAND script at a time in the future specified by the user

Command used: SCHTASKS
"""

import argparse
import calendar
import os
import sys
import time

from src import help
from src.initialize import Initialize

initializer = Initialize()
whiteSpace = initializer.whiteSpace


def main():
    cmd = sys.argv[0].partition(".")[0]

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('action', nargs='?')
    parser.add_argument('--help',
                        '-help',
                        action='store_true')

    args = parser.parse_args()

    if args.help:
        help.displayHelp(cmd)
        return

    if args.action == "add":
        addTask()
    elif args.action == "del":
        delTask()
    else:
        help.displayHelp(cmd)


def getCurrentTime():
    """ Returns the current time in 24 hr format """

    return time.strftime("%H:%M")


def getCurrentDate():
    """ Returns the current date in MM/DD/YYYY format """

    return time.strftime("%m/%d/%Y")


def isValidTime(givenTime, today):
    """ Given a time string this function checks if the given time is
    in the future today (if "today" is true) else just validates the time
    """

    givenTime = givenTime.split(":")
    currentTime = getCurrentTime().split(":")

    givenHour = int(givenTime[0])
    givenMinute = int(givenTime[1])

    currentHour = int(currentTime[0])
    currentMinute = int(currentTime[1])

    if today:
        if givenHour < 24 and givenMinute <= 59:
            return (
                (givenHour > currentHour) or
                (givenHour == currentHour and givenMinute > currentMinute)
            )
    else:
        return givenHour < 24 and givenMinute <= 59

    return False


def isValidDate(givenDate):
    """ Given a date string this function checks if the date is in the future
    """

    givenDate = givenDate.split("/")
    currentDate = getCurrentDate().split("/")

    givenDay = int(givenDate[1])
    givenMonth = int(givenDate[0])
    givenYear = int(givenDate[2])

    currentDay = int(currentDate[1])
    currentMonth = int(currentDate[0])
    currentYear = int(currentDate[2])

    try:
        calendar.weekday(givenYear, givenMonth, givenDay)
    except ValueError:
        return False

    return (
        (givenYear == currentYear and givenMonth == currentMonth and givenDay > currentDay) or
        (givenYear == currentYear and givenMonth > currentMonth) or
        (givenYear > currentYear))

    return False


def addTask():
    """ Takes all the information about the task to be scheduled and
    creates the scheduled task """

    commands = []

    # List of ALL the files present in the scripts directory
    scripts = os.listdir(os.getcwd())

    for script in scripts:
        # Appends all the script names that have "hs-" prefix and ".py" extension
        # to commands after removing the extension from the script name

        if script[0:3] == "hs-" and script.endswith(".py"):
            cmdName = script.partition(".")[0]
            commands.append(cmdName)

    while True:
        taskName = input("{} Task name: ".format(whiteSpace))

        if taskName:
            break
        else:
            print("{} Invalid task name".format(whiteSpace))

    while True:
        cmdName = input("{} Command name: ".format(whiteSpace))

        if cmdName in commands:
            break
        else:
            print("{} Invalid command".format(whiteSpace))

    while True:
        date = input("{} Date (leave blank if today) [MM/DD/YYYY]: ".format(whiteSpace))

        if date == "" or isValidDate(date):
            break
        else:
            print("{} Invalid date".format(whiteSpace))

    if date == "":
        date = getCurrentDate()

    while True:
        taskTime = input("{} Time [HH:MM]: ".format(whiteSpace))

        if date == getCurrentDate():
            check = isValidTime(taskTime, True)
        else:
            check = isValidTime(taskTime, False)

        if check:
            break
        else:
            print("{} Invalid time".format(whiteSpace))

    cmdName = os.path.join(os.getcwd(), cmdName + ".py")
    command = "SCHTASKS /CREATE /SC ONCE /TN {0} /SD {1} /ST {2} /TR \"python '{3}'\"".format(
        taskName,
        date,
        taskTime,
        cmdName)

    os.system(command)


def delTask():
    """Asks the user for the task name to delete and attempts to delete
    that task"""

    while True:
        taskName = input("{} Enter task name: ".format(whiteSpace))

        if taskName:
            break
        else:
            print("{} Invalid task name".format(whiteSpace))

    command = "SCHTASKS /DELETE /TN {}".format(taskName)

    os.system(command)


if __name__ == "__main__":
    main()
