# Author: Areeb Beigh
# Created: 23rd July 2016

"""
This script creates a new windows scheduled task that executes a hacker-scripts
COMMAND script at a time in the future specified by the user

Command used: SCHTASKS
"""

#############################################################################
#    Copyright (C) 2016  Areeb Beigh <areebbeigh@gmail.com>                 #
#                                                                           #
#    This program is free software: you can redistribute it and/or modify   #
#    it under the terms of the GNU General Public License as published by   #
#    the Free Software Foundation, either version 3 of the License, or      #
#    (at your option) any later version.                                    #
#                                                                           #
#    This program is distributed in the hope that it will be useful,        #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#    GNU General Public License for more details.                           #
#                                                                           #
#    You should have received a copy of the GNU General Public License      #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.  #
#############################################################################

# Python imports
import argparse
import calendar
import os
import re
import sys
import time

# Local imports
from src import help
from src.initialize import Initialize

initializer = Initialize()
white_space = initializer.white_space


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('action', nargs='?')
    parser.add_argument('--help',
                        '-help',
                        action='store_true')

    args = parser.parse_args()

    if args.action == "add":
        add_task()
    elif args.action == "del":
        del_task()
    else:
        cmd = sys.argv[0].partition(".")[0]
        help.display_help(cmd)
        return


def get_current_time():
    """ Returns the current time in 24 hr format """

    return time.strftime("%H:%M")


def get_current_date():
    """ Returns the current date in MM/DD/YYYY format """

    return time.strftime("%m/%d/%Y")


def is_valid_time(given_time, today):
    """
    Given a time string this function checks if the given time is
    in the future today (if "today" is true) else just validates the time
    """

    given_time = given_time.split(":")
    current_time = get_current_time().split(":")

    given_hour = int(given_time[0])
    given_minute = int(given_time[1])

    current_hour = int(current_time[0])
    current_minute = int(current_time[1])

    if today:
        if given_hour < 24 and given_minute <= 59:
            return (
                (given_hour > current_hour) or
                (given_hour == current_hour and given_minute > current_minute)
            )
    else:
        return given_hour < 24 and given_minute <= 59

    return False


def is_valid_date(given_date):
    """
    Given a date string this function checks if the date is in the future
    """

    given_date = given_date.split("/")
    current_date = get_current_date().split("/")

    given_day = int(given_date[1])
    given_month = int(given_date[0])
    given_year = int(given_date[2])

    current_day = int(current_date[1])
    current_month = int(current_date[0])
    current_year = int(current_date[2])

    try:
        calendar.weekday(given_year, given_month, given_day)
    except ValueError:
        return False

    return (
        (given_year == current_year and given_month == current_month and given_day > current_day) or
        (given_year == current_year and given_month > current_month) or
        (given_year > current_year))

    return False


def add_task():
    """
    Takes all the information about the task to be scheduled and
    creates the scheduled task
    """

    commands = []
    blank_line = r"^\s+$"

    # List of ALL the files present in the scripts directory
    scripts = os.listdir(os.getcwd())

    for script in scripts:
        # Appends all the script names that have "hs-" prefix and ".py" extension
        # to commands after removing the extension from the script name

        if script[0:3] == "hs-" and script.endswith(".py"):
            cmd_name = script.partition(".")[0]
            commands.append(cmd_name)

    while True:
        task_name = input("{} Task name: ".format(white_space))

        if task_name:
            break
        else:
            print("{} Invalid task name".format(white_space))

    while True:
        cmd_name = input("{} Command name: ".format(white_space))

        if cmd_name in commands:
            break
        else:
            print("{} Invalid command".format(white_space))

    while True:
        date = input("{} Date (leave blank if today) [MM/DD/YYYY]: ".format(white_space))

        if (re.search(blank_line, date) or date == "") or is_valid_date(date):
            break
        else:
            print("{} Invalid date".format(white_space))

    if re.search(blank_line, date) or date == "":
        date = get_current_date()

    while True:
        task_time = input("{} Time [HH:MM]: ".format(white_space))

        if date == get_current_date():
            check = is_valid_time(task_time, True)
        else:
            check = is_valid_time(task_time, False)

        if check:
            break
        else:
            print("{} Invalid time".format(white_space))

    cmd_name = os.path.join(os.getcwd(), cmd_name + ".py")
    command = "SCHTASKS /CREATE /SC ONCE /TN {0} /SD {1} /ST {2} /TR \"python '{3}'\"".format(
        task_name,
        date,
        task_time,
        cmd_name)

    os.system(command)


def del_task():
    """
    Asks the user for the task name to delete and attempts to delete
    that task
    """

    while True:
        task_name = input("{} Enter task name: ".format(white_space))

        if task_name:
            break
        else:
            print("{} Invalid task name".format(white_space))

    command = "SCHTASKS /DELETE /TN {}".format(task_name)

    os.system(command)


if __name__ == "__main__":
    main()
