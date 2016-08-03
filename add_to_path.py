"""
Adds the current working directory to environment variable PATH
"""

import os

absDirPath = os.path.dirname(os.path.abspath(__file__))
PATH = os.environ['PATH']

if absDirPath not in PATH.split(";"):
    os.system("setx PATH \"\"")
    os.system("setx PATH \"{0};{1}\"".format(PATH, absDirPath))

print("""
        The hacker-scripts has been added to PATH.
        -----
        To view the hacker-scripts commands from your terminal,
        open a new terminal window and type hs-help.
    """)
