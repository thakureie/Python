"""
This Programme will search file , delete line and update that file again
"""

import os, sys, re

search = sys.argv[1]
updatefile = sys.argv[2]

with open("/root/file1" , "r") as file:
    with open("/root/file2" , "w") as file1:
        new_file = file.readlines()
        file.seek(0)
        for line in new_file:
          if search not in line:
              file1.write(line)


with open("/root/file2", "a") as file3:
    file3.write(updatefile+"\n")
