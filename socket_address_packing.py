#!/usr/bin/python3
import binascii, socket, struct, sys

for string_address in ['192.68.1.1', '127.0.0.1']:
	packed = socket.inet_aton(string_address)
	print('Original: ', string_address)
	print('Packed:', binascii.hexlify(packed))
	print('Unpacked:', socket.inet_ntoa(packed))
	print()
