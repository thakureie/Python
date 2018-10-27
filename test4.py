f1 = open("/var/log/syslog", 'r')
f2 = open("/root/python/syslog2", 'w')
for line in f1:
     f2.write(line.replace("abhithak" , "SYSLO65"))
f2.close()
f1.close()
