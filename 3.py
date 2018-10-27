for line in open('/root/test'):
    if '/backup' in line:
        print(line)
