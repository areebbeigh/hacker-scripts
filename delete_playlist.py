"""
This script is used by hs-music to delete the temporary playlist it creates.

Since it may take some time for the music player to launch we cannot immediately
delete the playlist.m3u file after calling os.system() on it, hence, we wait for
20 seconds and then delete the playlist.

This script is separate because if it is put in hs-music.py then the user has to
wait for 20 seconds to use the command line again.
"""

# Python imports
import os
import time


def main():
    print("Deleting temporary playlist in")
    # The timer
    for i in range(0,20):
        time.sleep(1)
        i -= 20
        print("%s seconds\r" % i, end="")

    os.remove('playlist.m3u')

if __name__ == "__main__":
    main()