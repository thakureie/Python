#!/usr/bin/env python

import sys
import os
_file_name="/root/file"
_output_file="/root/file2"
_search_string="Ram is another Name\n"

print(_file_name)
print(_search_string)

with open(_file_name,'r') as file:
    for line in file:
        if line !=  _search_string:
            with open(_output_file,'a') as output_file:
                  output_file.write(line)

os.rename(_output_file,_file_name)
