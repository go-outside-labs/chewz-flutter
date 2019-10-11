#!/usr/bin/env python

import subprocess

if __name__ == "__main__":

    try:
        subprocess.call(["mkdir", "pictures"])
    except:
        pass

    subprocess.call(["ig_scrapper", "-t", "image", "--destination", "./pictures", "--filename", './restaurant_list.txt', "--media-metadata", '--profile-metadata', '--retain-username'])

