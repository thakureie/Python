"""
This Programme will take command line arguments , search line(string) in file , delete line and append/updtae that file again
sys.argv[1] = This is keyword/line which you want to search
sys.argv[2] = THis is file which is dummy)
sys.argv[3] = This is Souce file which will be searched
sys.argv[4] = This is destination file
"""

import os, sys, re

search = sys.argv[1]
#updatefile = sys.argv[2]

with open(sys.argv[2] , "r") as file:
    with open(sys.argv[3] , "w") as file1:
        new_file = file.readlines()
        file.seek(0)
        for line in new_file:
          if search not in line:
              file1.write(line)


with open(sys.argv[3], "a") as file3:
    file3.write("\n")
