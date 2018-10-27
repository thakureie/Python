#!/usr/bin/python
import os, subprocess
import socket
#host = str(subprocess.call("hostname", shell=True))
print(socket.gethostname())
host = socket.gethostname()
final_path = os.path.join('/root/', host, '/test1234' )
print(final_path)
if os.path.isdir(final_path):
    print("Directory exists", host)
elif os.path.isfile(final_path):
   print("File name is ", host)
else:
   print("File does not exists")

