import re
import sys
import glob

for arg in sys.argv[2:]:
	for file in glob.iglob(arg):
		for line in open(file, 'r'):
			if re.findall(sys.argv[1], line):
				print(line)
