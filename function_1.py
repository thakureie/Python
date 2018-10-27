import os, subprocess, shlex, re

host_type = str(input("Please enter host type: ")).upper()


		#output = str(subprocess.Popen(arg, shell=True, stdout = subprocess.PIPE).communicate()[0].strip())
		#command1 = "blkid;ls"
		#return output

def exec_cmd(cmd):
	cmd = shlex.split(cmd)
	output = str(subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE).communicate()[0].strip())
	return output

def ed_host():
	print("ED node commands")
	output = exec_cmd(cmd="pvdisplay;pvs;lvs")
	return output

def write_file(filename, output2):
	file = open(filename, 'w')
	lines = output2.split("\\n")
	for line in lines:
		file.write(line + "\n")
	file.close()

#output2 = exec_cmd(cmd="pvdisplay")
#write_file('ed1', output2)


if host_type == "ED" :
        print("This is Exadata system\n")
        print(ed_host())
	output2 = ed_host()
	write_file('ed', output2)



elif host_type == "BR":
     print("This is baremetal host\n")
elif host_type == "DOM0":
     print("This is Dom0 System\n")
elif host_type == "VM":
     print("This is VM\n")
else:
    print("Not sure on system type, Please check manually\n")




