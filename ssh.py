import sys, os, string, threading
import paramiko
cmd = "cat /etc/fstab"
outlock = threading.Lock()


def workon(host):
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh.connect(host, username='abhithak', password='Pawan1@jha')
  stdin, stdout, stderr = ssh.exec_command(cmd)
  stdin.write('xy\n')
  stdin.flush()
  
  with outlock:
	print(stdout.readlines())
	
	
def main():
    hosts = ['192.168.0.104'] 
    threads = []
    for h in hosts:
        t = threading.Thread(target=workon, args=(h,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

main()

