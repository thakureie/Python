#!/usr/bin/python
import sys

counter = 0
while True:
    line = sys.stdin.readline()
    if not  line:
        break
    print("%s: %s" % (counter, line))
    counter += 1
