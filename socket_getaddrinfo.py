#!/usr/bin/python
import socket

def get_constants(prefix):
	return {
		getattr(socket,n):n
		for n in dir(socket)
		if n.startswith(prefix)
	}

families = get_constants('AF_')
Types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

for response in socket.getaddrinfo('www.python.org', 'http'):
	Family, socktype, proto, cannonical, address = response
	print('Family:', families[Family])
	print('Scoket Type:', Types[socktype])
	print('Protocols:', protocols[proto])
	print('Cannonical Name:', cannonical)
	print('Socket Address:', address)
	print("===========================")
