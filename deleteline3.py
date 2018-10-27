import sys, os
search = sys.argv[1]

with open("/root/file1" , "r+") as f:
	new_f = f.readlines()
	f.seek(0)
	for line in new_f:
	   if search  not in line:
	     f.write(line)
	f.truncate()
