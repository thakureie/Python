import subprocess, os, re, sys

file = sys.argv[1]

with open(file , 'r') as file1:
	file2 = file1.read()

if sys.argv[2] in file2:
	print("FS is mounted")
else:
	print("FS is not mounted")
