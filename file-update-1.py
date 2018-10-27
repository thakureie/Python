f1 = open('file1.txt', 'r')
f2 = open('file2.txt', 'w')
for line in f1:
    f2.write(line.replace('swap', 'This is new line'))
f1.close()
f2.close()
