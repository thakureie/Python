#!/usr/bin/python
import sys
from sys import argv

script, filename = argv

print("We are going to earse file %r " % filename)

print("If you do not want to write in file, please use CTRL+C (^c)")
print("If you want to continue, HIT ENTER")
raw_input("?")

target = open(filename, 'w')

print("We are going to delete file content")
target.truncate()

print("We are writting three lines in file")
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Finally We are going to close file")
target.close()
