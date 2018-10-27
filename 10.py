#!/usr/bin/python
import subprocess
df = "df"
arg = "-hP"
print("This is mounted file System information  \n")
subprocess.call([df , arg])
print("Df ................. 2nd times")
subprocess.call(['df', '-hP'])
subprocess.call(["ls -al /tmp"] , shell=True)
