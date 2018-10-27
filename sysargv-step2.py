#!/usr/bin/python
import sys
num_arguments = len(sys.argv) -1

if num_arguments == 0:
	sys.stderr.write('Hey, type i option silly\n')
else:
	print(sys.argv, "You typed in ", num_arguments, "argument")
