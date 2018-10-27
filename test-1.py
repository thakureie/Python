#!/usr/bin/python
f1 = open("/var/log/syslog", 'r')
f2 = open("syslog", 'w')

for line in f1:
	f2.write(line.replace("abhithak", "ABHITHAK"))
f1.close()
f2.close()
