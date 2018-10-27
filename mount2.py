import subprocess, os, re, shutil, datetime, time

with open('/etc/fstab' , 'r') as file:
    file1 = file.read()

if 'swap' in file1:
    print("swap found")
else:
    print("Not found")

path = "/etc/fstab" + datetime.datetime.today().strftime("%Y-%m-%d")

if os.path.exists(path):
	print(path, "Already exists")
else:
	open(path, 'a').close()

shutil.copyfile("/etc/fstab", path)
