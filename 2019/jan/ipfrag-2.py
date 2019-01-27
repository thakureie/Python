#/usr/bin/python
import os,datetime,shutil,re
#file_path=/etc/sysctl.conf
file_path="/tmp/sysctl.conf"

num1 = 'net.ipv4.ipfrag_low_thresh = 15728640'
num = "net.ipv4.ipfrag_high_thresh = 16777216"

''' This Programme checks ipfrag value in /etc/sysctl.conf .
It also checks parameter in /proc/net/ip4

'''

date = datetime.datetime.today().strftime('%Y-%m-%d')
find_low_thresh=re.compile(r'^net.ipv4.ipfrag_low_thresh\s*=\s*15728640')
find_high_thresh=re.compile(r'^net.ipv4.ipfrag_high_thresh\s*=\s*16777216')
find_low_thresh1 = re.compile(r'^net.ipv4.ipfrag_low_thresh*')
find_high_thresh1 = re.compile(r'^net.ipv4.ipfrag_high_thresh*')
low_count=0
high_count=0
good_Lvalue=False
good_Hvalue=False
hTresh=False
lTresh=False
lt_list=[]
ht_list=[]
h_cleanNeeded=False
l_cleanNeeded=False

sysctlf=open(file_path,"r")
lines=sysctlf.readlines()
for line in lines:
	#create clean copy of the line for RE simplicty
	sline=''.join(line.split()).strip()
	#get sure the line is not commented out
	if sline.startswith('#'):
		continue
        for match in re.finditer(find_low_thresh1,sline):
                lt_list.append(line)
		hTresh=True
        for match in re.finditer(find_low_thresh,sline):
		good_Lvalue=True
        for match in re.finditer(find_high_thresh1,sline):
		ht_list.append(line)
		lTresh=True
        for match in re.finditer(find_high_thresh,sline):
		good_Hvalue=True
sysctlf.close()
print "hlist"+str(ht_list)
print "lt_list"+str(lt_list)
print '____________________________________________________'
if len(ht_list) == 1:
	if  good_Hvalue:
		print "high_thresh is correct:" +str(ht_list[0])
	else:
		print "High value present but incorrect value" +str(ht_list[0])
		h_cleanNeeded=True	
else:
	if len(ht_list)==0:
		print "High value is not present"
	if len(ht_list)>1:
		print "More than one High value found, cleanup will be needed"+str(ht_list)
		h_cleanNeeded=True


if len(lt_list) == 1:
        if  good_Lvalue:
                print "low_thresh is correct:" +str(lt_list[0])
        else:
                print "low value present but incorrect value" +str(lt_list[0])
		l_cleanNeeded=True

else:
        if len(lt_list)==0:
                print "low value is not present"
	if len(lt_list)>1:
                print "More than one LOW value found, cleanup will be needed"+str(lt_list)
		l_cleanNeeded=True
'''At this point 
if h_cleanNeeded==True  then comment out the ht_list entries and add the right value 
if l_cleanNeeded==True  then comment out the lt_list entries and add the right value
if not hTresh or h_cleanNeeded then add the right High value
if not lTresh or l_cleanNeeded then add the right low value
'''
