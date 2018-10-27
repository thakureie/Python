#!/usr/bin/python

import re

def run_re():
	pattern = "pDq"
	re_obj = re.complie(pattern)

infile = open('large_re_file.txt', 'r')
match_count = 0
lines = 0
for line in infile:
	match = re_obj
        if match:
            match_count += 1
	lines += 1
retrun(lines, match_count)


if _name_ == "_main_":
	lines, match_count = run_re()
	print ('LINES::', lines)
	print ('MATCHES::', match_count)
