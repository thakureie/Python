#/usr/bin/python
import re,shutil,os,inspect
from datetime import datetime
file_path = "/tmp/sysctl.conf"
	
''' This Programme fetches two parameter value mentioned Below.
If Parameter Matches no need to take any action 
If exact parameter does not match fix it.

net.ipv4.ipfrag_high_thresh = 16777216
net.ipv4.ipfrag_low_thresh = 15728640

'''

date = datetime.today().strftime("%d-%m-%Y")
backupfile=file_path + date

if os.path.isfile(backupfile):
	print("Backup Of ", backupfile, " already exists")
else:
	shutil.copyfile(file_path , backupfile)
	print("Backup Taken",backupfile)
ipfrag_low_thresh_c=re.compile(r'^net.ipv4.ipfrag_low_thresh\s*=\s*15728640$')
ipfrag_high_thresh_c=re.compile('^net.ipv4.ipfrag_high_thresh\s*=\s*16777216$')

ipfrag_low_thresh_j=re.compile(r'^net.ipv4.ipfrag_low_thresh*')
ipfrag_high_thresh_j=re.compile(r'^net.ipv4.ipfrag_high_thresh*')

lt_thresh = []
ht_thresh = []
lt_good=False
ht_good=False
lThresh=False
hThresh=False
good_Lvalue=False
good_Hvalue=False

h_cleanNeeded=False
l_cleanNeeded=False



sysctlf=open(file_path, 'r')
lines=sysctlf.readlines()


for line in lines:
	slines=''.join(line.split()).strip()
	if slines.startswith('#'):
		continue

	for match in re.finditer(ipfrag_low_thresh_j, slines):
		lt_thresh.append(line)
		hThresh=True
	for match in re.finditer(ipfrag_low_thresh_c, slines):
		good_Lvalue=True
	for match in re.finditer(ipfrag_high_thresh_j, slines):
		ht_thresh.append(line)
		lThresh=True
	for match in re.finditer(ipfrag_high_thresh_c, slines):
		good_Hvalue=True


sysctlf.close()

print("lt_thresh" + str(lt_thresh))
print("ht_thresh" + str(ht_thresh))
print("---------------------------------------------")


if len(ht_thresh) == 1:
	if good_Hvalue:
		print("Good High Threshold is:" + str(ht_thresh[0]))
	else:
		print("High value present but cleanup needed")
		h_cleanNeeded=True

else:
	if len(ht_thresh) == 0:
		print("High Thresh does not exists")
	if len(ht_thresh)> 1:
		print("More than 1 high value present, cleanup needed" +str(ht_thresh[0]))
		h_cleanNeeded=True


if len(lt_thresh) == 1:
	if good_Lvalue:
		print("Good Low Value is present:" + str(lt_thresh[0]))
	else:
		print("Low value is present but cleanup Needed"+ str(lt_thresh[0]))
		l_cleanNeeded=True

else:
	if len(lt_thresh) == 0:
		print("Low value not present")
	if len(lt_thresh)>1:
		print("More than 1 low value present"+ str(lt_thresh[0]))
		l_cleanNeeded=True



if h_cleanNeeded:
	for line in ht_thresh:
		lines.pop(lines.index(line))

if l_cleanNeeded:
	for line in lt_thresh:
		lines.pop(lines.index(line))

if not hThresh or h_cleanNeeded:
	lines.append('net.ipv4.ipfrag_high_thresh = 16777216\n')
if not lThresh or l_cleanNeeded:
	lines.append('net.ipv4.ipfrag_low_thresh = 15728640\n')

out=open(file_path, 'w')
out.writelines(lines)
out.close()

