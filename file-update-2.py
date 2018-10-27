f = open("filein", 'r')
filedata = f.read()
f.close()

newdata = filedata.replace("file", "directory")

f = open("fileout", 'w')
f.write(newdata)
f.close()
