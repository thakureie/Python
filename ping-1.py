import subprocess
ip = input("Please enter your IP: ")
type(ip)
cmd = "ping -c 3 "+ ip
if (subprocess.call(cmd , shell=True) == 0):
   print("Your is alive")
else:
   print("Not alive")

