#!/usr/bin/python
f = open("/var/log/syslog" , 'r')
filedata = f.read()
f.close()

newdata = filedata.replace("abhithak" , "SYSLOG")

f2 = open("syslog1", 'w')
f2.write(newdata)
f2.close()
