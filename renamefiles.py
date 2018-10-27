#!/usr/bin/python

from diskwalk_api import diskwalk

from shutil import move

files = diskwalk("/tmp")

for file in files:
	if fnmatch(file, "*.txt"):
	#here we can do anuthing we want, delete, mobe rename.... hmm rename
		move(file, "%s.mp3" % file)

