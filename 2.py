with open('/root/test', 'r') as f:
    for line in f:
        if '/u02'  in line:
            print (line)
