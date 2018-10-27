#!/usr/bin/python
import subprocess
def dffunc():
	subprocess.call("df -hP", shell=True)

print (":::::::::::::::::::::::::::::::")
def uname():
	subprocess.call("uname -a", shell=True)

def main():
	dffunc()

	uname()
main()
