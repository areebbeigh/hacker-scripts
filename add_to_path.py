"""
Adds the current working directory to environment variable PATH
"""

import os

currentDir = os.getcwd()
PATH = os.environ['PATH']

if currentDir not in PATH.split(";"):
    os.system("setx PATH \"\"")
    os.system("setx PATH \"{0};{1}\"".format(PATH, currentDir))

print("""
        This directory has been added to PATH.
        -----
        To view the hacker-scripts commands from your terminal,
        open a new terminal window and type hs-help.
    """)
