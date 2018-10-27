f = open('/root/test', 'r')
for line in f.readlines():
    if '/fsnadmin' not in line:
        print(line)
