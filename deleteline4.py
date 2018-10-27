""" This program searches exact line and delete that partucular line and saves file
"""
import sys, os
search = sys.argv[1]
with open("/root/file1" , "r") as file:
  with open("/root/file2", 'w') as file2:
    new_file = file.readlines()
    file.seek(0)
    for line in new_file:
      if search not in line:
	file2.write(line)
       # file2.close()
  #file.truncate()
