#/usr/bin/python
import os,datetime,shutil,re

num1 = 'net.ipv4.ipfrag_low_thresh = 15728640'
num = "net.ipv4.ipfrag_high_thresh = 16777216"

''' This Programme checks ipfrag value in /etc/sysctl.conf .
It also checks parameter in /proc/net/ip4

'''

date = datetime.datetime.today().strftime('%Y-%m-%d')
find_low_thresh=re.compile(r'net.ipv4.ipfrag_low_thresh\s*=\s*15728640')
find_high_thresh=re.compile(r'net.ipv4.ipfrag_high_thresh\s*=\s*16777216')
find_low_thresh1 = re.compile(r'net.ipv4.ipfrag_low_thresh*')
find_high_thresh1 = re.compile(r'net.ipv4.ipfrag_high_thresh*')
low_count=0

for i, line in enumerate(open("/etc/sysctl.conf", "r")):
	for match in re.finditer(find_low_thresh1,line):
		print(match.group())
		S3=match.group()
		print(S3)
		low_count+=1


if low_count == 0:
	print("Count is Zero and no match found")
        with open("/etc/sysctl.conf", "a") as myfile:
		myfile.write( "net.ipv4.ipfrag_low_thresh = 15728640\n")


elif low_count == 1:
	print("Counter is one")
	with open("/etc/sysctl.conf", "a") as myfile:
		myfile.write(re.sub("net.ipv4.ipfrag_low_thresh","net.ipv4.ipfrag_low_thresh = 15728640\n"))
else:
	print("Do Nothing")

#####################################################

if os.path.isfile("/etc/sysctl.conf." + date):
	print("File already exists")
else:
	print("It Does not exists,Copying file")
	shutil.copy("/etc/sysctl.conf", "/etc/sysctl.conf."+date)

if os.path.isfile("/etc/sysctl.conf." + date):
	S2="File already exists"
	print(S2)

else:
	print("File copiped")
