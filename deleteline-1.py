import sys, os, re


search = "Ram is another Name1\n"
print("/root/file2")

with open("/root/file", "r") as file:
	for line in file:
		if line != search:
        		with open("/root/file2", "w") as output_file:
                		output_file.write(line)

#os.rename("/root/file2" , "/root/file4")
