import socket
abc = str(input("Enter FQDN: "))
ip = socket.gethostbyname(abc)
print("IP of", abc ," is", ip )
