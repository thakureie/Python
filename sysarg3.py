import os, sys, subprocess,re


def exec_cmd(cmd):
	#cmd = shlex.split(cmd)
	#cmd = sys.argv[1]
	output = str(subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE).communicate()[0].strip())
	return output
cmd = sys.argv[1]
#print(exec_cmd(cmd))

output = exec_cmd(cmd)
file1 = sys.argv[2]
file = open(file1, "r")

for line in file:
	if re.search(sys.argv[3], line):
		print(line)

