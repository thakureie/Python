# strings and bytes are not directly interchnagable
# Strings contain unicode,bytes are raw 8-bit values


def main():
	# Define some starting values
	b = bytes ([0x41, 0x42, 0x43, 0x44])
	print(b)

	s = " This is a string"
	print(s)
	


#TODO: Try combining them.
	#print( b.decode('utf-8') + s )
	#s2 = b.decode('utf-8')
	#print(s+s2)

#TODO: Bytes and strings need to ne properly encoded and decoded
#Before you can work on them together

	#s3 = s.encode('utf-8')
	#print(b+s3)
#TODO: encode the strings as UTF-32
	s4 = s.encode('utf-32')
	print(s4 )

if __name__ == "__main__":
	main()
