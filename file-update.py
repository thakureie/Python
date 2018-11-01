f = open("filein",'r')
filedata = f.read()
f.close()

#newdata = filedata.replace("old data","new data")
newdata = filedata.replace("nfsvers=3","nfsvers=100")

f1 = open("fileout",'w')
f1.write(newdata)
f1.close()
