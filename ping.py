import subprocess
ip = input("Please enter your IP: ")
type(ip)
if (subprocess.call("ping -c 3 " + ip ,stdout = subprocess.PIPE, shell=True) == 0):
   print("Your is alive")
else:
   print("Not alive")

