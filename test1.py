#!/usr/bin/env python
#A System Information Gathering Script
import subprocess

#command1
uname = "uname"
uname_arg = "-a"
print("Gathering system information with %s command :\n" % uname)
subprocess.call([uname, uname_arg])
print("..............")
subprocess.call(["uname", "-a"])
