with open('2' , 'r') as f:
  file_lines = [''.join([x.rstrip(),"(", x, "\n"]) for x in f]
with open('3' ,'w') as f1:
  f1.writelines(file_lines)

