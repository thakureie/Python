#!/usr/bin/python

import sys

for i, line in enumerate(sys.stdin):
	print("%s: %s" % (i, line))
