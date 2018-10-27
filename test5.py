f1 = open("/var/log/syslog" , 'r')
f2 = f1.read()
f1.close()

#new1 = f2.replace("abhithak" , "ABHITHAK100")

f3 = open("/root/python/syslog3" , 'w')
f3.write(f2.replace("abhithak" , "100ABHITHAK100"))
f3.close()
