# hacker-scripts

<img src="http://i.imgur.com/q0McDj7.png">
<img src="http://i.imgur.com/VpmObpa.png">

hacker-scripts is a collection of mini-scripts written in Python intended to make frequently used or random tasks such as playing music, 
launching programs you use frequently, opening the pages you browse daily etc just with a single command through your terminal.

These scripts can be re-configured anytime just by editing an easy to use .ini configuration file.

## Installation
The `setup.py` script first creates a directory tree - hacker-scripts\bin in your root directory and then copies different scripts
from `src` to their respective locations. After this hacker-scripts and hacker-scripts\bin are added to your PATH so that they can be
accessed directly from the terminal with ease.

To install hacker-scripts run `> python setup.py install`

Note: After installation you will have to close the terminal and open a new one to use any of the commands. If you are not able to use the
commands i.e you get a "command does not exist" kind of error then add C:\hacker-scripts and C:\hacker-scripts\bin (Windows) to your PATH
manually.

To view the help documentation type `hs-help` and hit enter.

## Configuration
Once you're done with the installation you will have to configure hacker-scripts. If the installation went well the process should be
quite simple, all you have to do is run `hs-config` in a new terminal window and the script will create a `config.ini` file in 
C:\hacker-scripts. 

After this the config.ini file will open (if it does not open automatically then navigate to your root directory >> hacker-scripts >> config.ini).

Here you can configure different scripts according to your needs. Below is an example configuration.

```ini
# You can add as many parameters as you want to CERTAIN sections but they must be in series
[hs-browse]
url1 = www.github.com
url2 = www.stackoverflow.com

[hs-music]
directory = C:\Users\Areeb\Desktop\Music

[hs-desktop]
files_directory = C:\Users\Areeb\Desktop\Files
images_directory = C:\Users\Areeb\Desktop\Media\Images
videos_directory = C:\Users\Areeb\Desktop\Media\Videos

[hs-start]
program1 = C:\Users\Areeb\Desktop\mIRC\mIRC.exe

[hs-wallpaper]
directory = C:\Users\Areeb\Desktop\Wallpapers

[hs-work]
project1 = C:\Users\Areeb\Desktop\Python\My Stuff\Under Development Projects\Python 3\RSS2IRC\rss2irc.py
```

## Usage
As I mentioned before, you can use any of the scripts included in hacker-scripts from your terminal. To get a list of the scripts
and their functions type `hs-help` in the terminal and hit enter.

## Possible Snag(s)
Sometimes the setup may not be able to add the directories C:\hacker-scripts and C:\hacker-scripts\bin to the system PATH, in that case
you will have to do this manually.

<a href="www.windowsitpro.com/systems-management/how-can-i-add-new-folder-my-system-path">
Here's a tutorial on adding directories to PATH (Windows)</a>

## Contributing
Feel free to fork the repository and include your own hacker-scripts or make any improvisations in the code. Once done you can make a pull
request. Make sure to add the script description in the `hs-help.py` script and also a detailed description of your script or/and the 
improvisations you made in the script(s).

Cheers :coffee:
<hr>
**Developer**: Areeb Beigh<br>
**Website**: <a href="http://www.areeb-beigh.tk" target="_blank">www.areeb-beigh.tk</a><br>
**Mail:** areebbeigh@gmail.com<br>
**Version**: 2.0 <br>
**GitHub Repo:** https://github.com/areeb-beigh/hacker-scripts
