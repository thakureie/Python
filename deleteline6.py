search = "Ram is another Name"
with open("/etc/fstab1", 'r') as f:
  with open("/etc/fstab2", 'w') as f1:
    new_f = f.readlines()
    f.seek(0)
    for line in new_f:
      if search not in line:
        f1.write(line)
    

