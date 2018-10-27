#!/usr/bin/python3
import sys
print("Arguments:", len(sys.argv))
print("List:", str(sys.argv))

if len(sys.argv) < 2:
	print("To few arguments, plz specify a filename")
else:
	filename = sys.argv[1]
	print("Arguents are : ", filename)
	 
