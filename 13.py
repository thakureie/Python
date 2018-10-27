#!/usr/bin/python
import subprocess
#res = subprocess.Popen(['uname', '-sv'], stdout=subprocess.PIPE)
#res = subprocess.Popen((['uname -a'], shell=True), stdout=subprocess.PIPE )
res = subprocess.Popen('uname -sv', shell=True, stdout=subprocess.PIPE)
uname = res.stdout.read().strip()
print(uname)
