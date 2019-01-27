#/usr/bin/python
import argparse,os,socket
parser = argparse.ArgumentParser(description="This will collect diffrent commands out from system", add_help=False)
group = parser.add_mutually_exclusive_group()
group.add_argument("-df" , "--df" , action="store_true")
group.add_argument("-version" , "--version" , action="store_true")
group.add_argument("-vm", "--vm", action="store_true")
group.add_argument("-vmmem", "--memory-vm", action="store_true")
group.add_argument("-dom0mem", "--dom0mem", action="store_true")
netstat_parser = argparse.ArgumentParser(parents=[parser])
netstat_parser.add_argument("-netstat", "--netstat", action="store_true")
netstat_parser.parse_args(['--netstat', 'YYYY'])

args = parser.parse_args()
uname = socket.gethostname()

if args.df:
	print("Below FS are mounted Currently on", uname )
	print("-" * 80)
	os.system("df")

if args.netstat:
	print("This seems better")
