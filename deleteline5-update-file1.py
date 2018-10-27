"""
This Programme will take command line arguments , search line(string) in file , delete line and append/updtae that file again
"""

import os, sys, re

search = sys.argv[1]
updatefile = sys.argv[2]

with open(sys.argv[3] , "r") as file:
    with open(sys.argv[4] , "w") as file1:
        new_file = file.readlines()
        file.seek(0)
        for line in new_file:
          if search not in line:
              file1.write(line)


with open(sys.argv[4], "a") as file3:
    file3.write(updatefile+"\n")
