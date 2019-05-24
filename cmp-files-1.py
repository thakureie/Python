#This will shows details of both files in + - Format in each line#
import difflib
with open('fil3.txt', 'r') as file1:
 with open('fil4.txt', 'r') as file2:
  with open('/tmp/1.txt', 'w') as file3_out:
   for line in difflib.Differ().compare(file1.readlines(), file2.readlines()):
    print(line)
    file3_out.writelines(line)


#Another way of same prgramme#

with open('fil3.txt', 'r') as file1:
 with open('fil4.txt', 'r') as file2:
  delta = difflib.Differ().compare(file1.readlines(), file2.readlines())
  print("Showing Diffrence ")
  print("=====================")
  print('\n'.join(delta))
