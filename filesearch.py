import re
f1 = open('/tmp/1', 'r')
search1 = re.compile(r'\d.*')

for line in re.findall(search1, f1.read()):
 print(line)
