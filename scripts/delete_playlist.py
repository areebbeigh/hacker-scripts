'''
This script is used by hs-music to delete the temporary playlist it creates.

Since it may take some time for the music player to launch we cannot immediately 
delete the playlist.m3u file after calling os.system() on it, hence, we wait for
20 seconds and then delete the playlist. 

This script is seperate because if it is put in hs-music.py then the user has to 
wait for 20 seconds to be able to use the command line again.
'''

import os
import time 
import sys

# Gets the root directory (Drive letter in case of windows)
rootDirectory = os.path.splitdrive(sys.executable)[0]

# Changes the current working directory
os.chdir(os.path.join(rootDirectory, "\\hacker-scripts"))

print("Deleting temporary playlist in")

# The timer
for i in range(0,20):
    time.sleep(1)
    i -= 20
    print("%s seconds\r" % i, end="")

os.remove('playlist.m3u')