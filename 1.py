#!/usr/bin/python3

file = open('/root/test', 'r')
for line in file:
    if '/fsnadmin' in line:
        print(line)
