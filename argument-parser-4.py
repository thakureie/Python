#!/usr/bin/python
import argparse,os,socket,platform,shutil
host = socket.gethostname()
dom0_parser = argparse.ArgumentParser(description="This takes o/p",add_help=False)
dom0_parser.add_argument("-dom0", "--dom0", action="store_true")
exadata_parser = argparse.ArgumentParser(parents=[dom0_parser])
exadata_parser.add_argument("-ed", "--exadata", action="store_true")

df_parser = argparse.ArgumentParser(add_help=False, parents=[exadata_parser])
df_parser.add_argument("-a", "--all", action="store_true")
args = df_parser.parse_args()

ibnodes_dx1 = "ibnodes  |grep"
ibnodes_dx2 = """x |awk '{print $6 "" }' |cut -d '"' -f2 |sort"""

path  = "/fsnadmin/" + host +"/"

if not os.path.isdir(path):
	os.mkdir(path)

def copyconfig():
	shutil.copy("/etc/mail/sendmail.cf" , path)
	shutil.copy("/etc/facter/facts.d/Puppet_Facts.yaml", path)
	shutil.copy("/etc/fstab", path)
	

def emptyformat():
	print("=*=" * 50)





def vmlist():
	print("Running VM is below ")
	os.system('xm list')

def brctl():
	print("Brdges information on Dom0 is below")
	os.system("brctl show")

def generic():
	print("PVS, LVS and other O/P")
	emptyformat()
	os.system('pvs')
	emptyformat()
	os.system('lvs')
	emptyformat()
	os.system('vgs')
	emptyformat()
	os.system('pvdisplay -v')
	emptyformat()
	os.system('lvdisplay -v')
	emptyformat()
	os.system('vgdisplay -v')
	emptyformat()
	os.system('/sbin/chkconfig --list | grep kdump')
	emptyformat()
	print("Routing Tables information ")
	emptyformat()
	os.system('netstat -nr')
	emptyformat()
	print("**** Below File Systems are Mounted ****")
	os.system('df -hP')
        print("Kenel version of ", host , "is below")
        print(platform.release())

	


def exadata():
	emptyformat()
	os.system("imageinfo")
	emptyformat()
	os.system("DB Nodes Running is ")
	os.system(ibnodes_dx1 + ' d'+ibnodes_dx2)
	emptyformat()
	print("Cell nodes Running is")
	os.system(ibnodes_dx1 + ' c'+ibnodes_dx2)	
	emptyformat()
	print("IB-Switch Running is ")
	os.system('ibswitches')
	
	
	
if args.exadata:
	print("Calling Exadta Related")
	print("=" * 70 )
	copyconfig()
	generic()
	exadata()


if args.dom0:
	print("=" * 70)
	copyconfig()
        generic()
	vmlist()
	brctl()

if args.all:
        print("=" * 70 )
	print("Calling Both ED and Dom0 Function")
        copyconfig()
        generic()
        exadata()
	vmlist()
	brctl()
