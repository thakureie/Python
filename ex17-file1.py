#!/usr/bin/python
from sys import argv
from os.path   import  exists

script, from_file, to_file = argv

print("We are going to copy from %s to %s" %  (from_file, to_file))
print("If you do not want to continue please press CTRL+C (^c)")
print("If you want to conitine hit ENTER")
raw_input("?")

in_file = open(from_file)
indata = in_file.read()
print("Files does have %d bytes and size is " % len(indata))

print("Does the output file is already exist %r" % exists(to_file))
print("Ifyou want to continue hit ENTER else CTRL+C to quit")

outdata = open(to_file, 'w')
outdata.write(indata)
outdata.close()
print("Allright, We are done")
