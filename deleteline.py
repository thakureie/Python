with open("/root/file1" , "r") as input1:
	with open("/root/file2" , "w") as output:
		for line in input1:
			if line != "Ram is another Name" + "\n":
				output.write(line)
