import os, socket, subprocess
host = socket.gethostname()
path = "/root/" + host + '/'
if os.path.exists(path):
     print(path, "Already exists")
else:
    os.mkdir(path)
    

def get_stdout(arg):
      output = str(subprocess.Popen(arg, shell=True, stdout = subprocess.PIPE).communicate()[0].strip())
      return output


def write_file(filename, output):
	file = open(path + filename , 'w')
	lines = output.split("\\n")
	for line in lines:
		file.write(line.replace("b'","") + "\n")
	file.close()

command = "uname -a"
output = get_stdout(command)
write_file(command.split(' ')[0], output)

command = "imageinfo"
output = get_stdout(command)
write_file(command, output)


command = "pvs"
output = get_stdout(command)
write_file(command, output)

command = "lvs"
output = get_stdout(command)
write_file(command, output)

command = "vgs"
output = get_stdout(command)
write_file(command, output)


command = "pvdisplay -v"
output = get_stdout(command)
write_file(command.split(' ')[0], output)

command = "lvdisplay -v"
output = get_stdout(command)
write_file(command.split(' ')[0], output)

command = "vgdisplay -v"
output = get_stdout(command)
write_file(command.split(' ')[0], output)

command = "netstat -nr"
output = get_stdout(command)
write_file(command.split(' ')[0], output)


command = "/sbin/chkconfig --list | grep kdump"
output = get_stdout(command)
write_file(command.split(' ')[0], output)

