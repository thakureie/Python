import os,sys,shutil
f = open(sys.argv[1], 'r')
filedata = f.read()
f.close()

#newdata = filedata.replace("old data","new data")
newdata = filedata.replace(sys.argv[2],sys.argv[3])

f1 = open(sys.argv[4], 'w')
f1.write(newdata)
f1.close()
