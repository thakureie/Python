#This will show only diffrence lines"

with open('fil3.txt', 'r') as file1:
 with open('fil4.txt', 'r') as file2:
  same = set(file1).symmetric_difference(file2)
same.discard('\n')

with open('some_output_file.txt' ,'w') as file_out:
 for line in same:
   file_out.write(line)
   print(line)

print(same)
