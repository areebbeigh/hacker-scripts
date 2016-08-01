# Author: Areeb Beigh
# Created: 23rd June 2016

"""
Prints a brief help documentation to the terminal
"""


def main():
    print("""
    Python hacker-scripts by Areeb - github.com/areeb-beigh/hacker-scripts (Feel free to contribute)

    This is a collection of mini-scripts written in Python intended to make
    frequently used or random tasks such as playing music, launching programs you use
    frequently, opening the pages you browse daily etc easier just with a single command 
    through your terminal.

    ---------
    Currently available commands:

    > hs-backup         Creates a backup of all the files in the backup location, both are specified in the config
    > hs-browse         Opens the URLs in the configuration file
    > hs-config         Creates (or overwrites) a config.ini file in the hacker-scripts directory
    > hs-desktop        Manages your desktop files by placing different file types to their respective directories
    > hs-help           Displays this help documentation
    > hs-music          Creates and plays a temporary playlist of music files in the directories in the configuration
    > hs-schedule       Creates a new windows scheduled task that executes a hacker-scripts cmd at a time in the future
    > hs-start          Launches the programs listed in the configuration
    > hs-wallpaper      Chooses and sets a random wallpaper from the wallpapers directory specified in the configuration
    > hs-work           Opens all the files specified with the text editor (both are set in the configuration)

    Most the above scripts depend on the config.ini file located in the hacker-scripts directory.
    If you don't find a config.ini file in your hacker-scripts directory run hs-config to create one.
    
    To view individual help documentation of any command use the following syntax:
    "<command name> -h"

    Ex: "hs-music -h" will display hs-music's help documentation.
    """)


if __name__ == "__main__":
    main()
