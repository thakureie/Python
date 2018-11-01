import subprocess,os
FNULL = open(os.devnull, 'w')
ip = input("Please enter your IP: ")
type(ip)
cmd = "ping -c 3 "+ ip
if (subprocess.call(cmd , stdout=FNULL,shell=True) == 0):
   print("Your is alive")
else:
   print("Not alive")

subprocess.call("ping -c 3 127.0.0.1", shell=True)
