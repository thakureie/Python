import os,re,subprocess,sys
file = open(sys.argv[1], 'r')
file1 = file.read()
find = re.findall(r"swap", file1, re.MULTILINE)

if "swap" in file1:
	print("found")
else:
	print("Not found")



