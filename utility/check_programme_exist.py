#!/usr/bin/python

import subprocess
import os

def check_programme_exist(name):
    try:
        devnull = open(os.devnull)
        subprocess.Popen([name], stdout=devnull, stderr=devnull).communicate()
    except OSError as e:
        if e.errno == os.errno.ENOENT:
           	return False
    return True


if check_programme_exist("stracex"):
	print("stracex is installed")
else:
	print("stracex is not installed")