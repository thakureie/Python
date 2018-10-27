import os,socket,subprocess, sys
host = os.popen("hostname -s").read().strip()
path = "/root/" + host



if os.path.isdir(path):
  print(path," exists")
else:
	os.mkdir(path)
	
def get_stdout(arg):
		output = str(subprocess.Popen(arg, shell=True, stdout = subprocess.PIPE).communicate()[0].strip())
		return output


def write_file(filename, output):
	file = open(path + '/'+ filename, 'w')
	lines = output.split("\\n")
	for line in lines:
		file.write(line.replace("b'","") + '\n')
	file.close()
	
command = "uname -a"
output=get_stdout(command)
write_file(command.split(' ')[0], output)


command = "df -hP"
output=get_stdout(command)
write_file(command.split(' ')[0], output)

command = "pvs"
output=get_stdout(command)
write_file(command.split(' ')[0], output)

command = "vgs"
output=get_stdout(command)
write_file(command.split(' ')[0], output)

command = "lvs"
output=get_stdout(command)
write_file(command.split(' ')[0], output)


