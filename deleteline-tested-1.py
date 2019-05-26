#!/usr/bin/python
import sys, os, re
search = re.compile(r"^Ram")

file1 = open("/root/file", "r")
file2 = file1.readlines()
file3 = open("/root/file2",  "w")
file4 = open("/root/file2-a", "w")
file5 = open("/root/file2-b", "w")

print("This is 1st code Block")

for line in file2:
	if not search.search(line):
		print(line)
		file3.writelines(line)
file3.close()         


print("This is 2nd Code Block")
for line in file2:
	if not search.search(line):
		print(line)
		file4.writelines(line)
file4.close()


print("This is 3rd code block")

for line in file2:
	finds = search.sub("Abhimanyu", line)
	print(finds)

print("This is 4th Code block")

for line in file2:
	if search.search(line):
		print(line)
		file5.writelines(line)
file5.close()


print("5th Block")

with open("/root/file" , "r") as file6:
	for line in file6:
		find1 = search.sub("Thakur", line)
		print(find1)
