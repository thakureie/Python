#!/usr/bin/pyton
from sys import argv
from os.path import exists

script, filename = argv

print("We are going to read %s" % filename)

file1 = open(filename, 'r')
file2 = file1.read()
print(file2)
file3 = open(filename, 'w')


if "swap"  in file2:
	print("File does have SWAP partition")
	file4 = file3.write("New Line is update and fstab entry is deleted\n")
else:
	print("No Swap partition")
file3.close()
print(file4)
file5 = open(filename, 'r')
file6 = file5.read()
print(file6)
