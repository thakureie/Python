#!/usr/bin/python3
import subprocess
subprocess.call('df')
b=subprocess.check_output(['ls', '-al' , '/tmp'])
c=subprocess.check_output(['uname', '-a'])
print(b)
print(c)
print("...................................")
subprocess.call("uname -a", shell=True)
