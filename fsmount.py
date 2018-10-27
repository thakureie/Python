import os, sys,re, subprocess
file = open('/proc/mounts' , 'r')
file1 = file.read()

if re.search(r"/media/sf_Desktop", file1):
	print("File System is mounted")
else:
	print("FS is not mounted")

def exec_cmd(cmd):
	output = str(subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE).communicate()[0].strip())
	return output

output = exec_cmd(cmd="df -hP")
lines = output.split("\\n")

for line in lines:
	print(line.replace("b'",""))
