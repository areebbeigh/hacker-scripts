# Author: Areeb Beigh
# Created: 23rd June 2016

'''
Prints a brief help documentation to the terminal
'''

def main():
    print("""
    Python hacker-scripts by Areeb - github.com/areeb-beigh

    This is a collection of mini-scripts written in Python intended to make
    frequently used or random tasks such as playing music, launching programs you use
    frequently, opening the pages you browse daily etc just with a single command through your 
    terminal.

    ---------
    Currently available commands:

    > hs-browse         Opens the URLs you specify in config.ini with the default browser
    > hs-config         Creates a new config.ini file in C:\hacker-scripts
    > hs-desktop        Manages your desktop files by placing different file types to their respective directories
    > hs-help           Displays this help documentation
    > hs-music          Creates and launches a temporary playlist of the mp3 files in the directory specified in config.ini
    > hs-start          Launches the programs listed in config.ini
    > hs-wallpaper      Chooses and sets a random wallpaper from the wallpapers directory specified in config.ini
    > hs-work           Opens all the files specified in config.ini

    All the above scripts depend on the config.ini file located in C:\hacker-scripts. You can edit the file anytime and
    the scripts will automatically run according to the new configuration.
    """)

if __name__ == "__main__":
    main()