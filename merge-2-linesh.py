with open("/root/15") as f:
    content = f.readlines()
    str = ""
    for i in range(1,len(content)+1):
        str += content[i-1].strip()
        if i % 3 == 0:
            print( str)
            str = ""
