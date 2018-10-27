import os, subprocess, shlex, shutil

host_type = input("Please enter hots type: ").upper()

host_name = os.popen("hostname -s").read().strip()

path = "/fsnadmin/" + host_name + "/"

if os.path.exists(path):
	print(path, " Already exists")
else:
   os.makedirs(path)




def exec_cmd(cmd):
	#cmd = shlex.split(cmd)
	output = str(subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE).communicate()[0].strip())
	return output


#def exec_cmd(cmd):
 #   cmd = shlex.split(cmd)
  #  subps = subprocess.Popen(cmd,stdout=subprocess.PIPE)
   # output = subps.communicate()[0].strip().split("\n")
   # return output

def write_file(filename, output):
    file = open(filename, 'w')
    lines = output.split("\\n")
    for line in lines:
        file.write(line + "\n")
    file.close()

def ed_host():
    output = exec_cmd(cmd="imageinfo;pvs")
    return output

def br_host():
	output = exec_cmd(cmd="uname -a;cat /etc/redhat-release;pvs;lvs;vgs;lvdisplay;pvdisplay;vgdisplay;df -hP;netstat -nr")
	return output

if host_type == "ED":
    print("This is exadata system")
    print(ed_host())
    output = ed_host()
    write_file(path +'edoutput', output)

if host_type == "BR":
	print("This is baremetal host")
	print(br_host())
	output = br_host()
	write_file(path + 'broutput', output)

#shutil.copy("/etc/fstab", path + '/fstab')
#shutil.copytree("/etc", path + 'etc')

def copy_config():
	shutil.copy("/etc/fstab", path + '/fstab')
	shutil.copy("/etc/mail/sendmail.cf", path + "/sendmail.cf")
	shutil.copy("/etc/facter/facts.d/Puppet_Facts.yaml", path + "Puppet_Facts.yaml")
	shutil.copytree("/etc", path + 'etc1')

copy_config()
print(copy_config())

