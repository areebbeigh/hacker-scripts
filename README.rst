hacker-scripts
===============

hacker-scripts is a collection of various scripts written in Python that make daily computer tasks easier. It is a great tool
if you are a lazy computer user (like me) and want things done just with a single command from your command line. This software 
currently mostly contains scripts that work on Windows OS. 


Installation
-------------

Simply download the hacker-scripts package and run the ``add_to_path.py`` script. This will add the hacker-scripts folder to the
environment variable PATH. After this you should be able to run any of the ``hs-`` prefixed hacker-scripts from the PowerShell
just by typing their name.

After adding the directory to PATH the next thing you have to do is to configure hacker-scripts. This also is an easy process,
to configure hacker-scripts run the ``hs-config`` command and a new config.ini file will be created in the hacker-scripts
directory. Once this is done you can proceed with the configuration. The configuration also is a straight forward process, the 
help docs are all available in the ``docs`` folder, you can refer to those for help.

Usage
-----

Using these scripts is pretty much straight forward. After you've done the installation process you can run any hacker-scripts
command via the command line (preferrable Windows PowerShell). Use `hs-help` to view a list of commands and use the following
syntax to get a detailed help description of a command:
``<command name> -dh`` example: ``hs-music -dh``
To simply view the syntax of a command use the following syntax: ``<command name> -h``

Contributing
------------

All contributions are welcomed. You can fork the repo add your own scripts (written in Python3) or bug fixes and make a pull request.

Cheers :coffee:

| **Developer:** Areeb Beigh
| **GitHub Repo:** https://github.com/areebbeigh/hacker-scripts
