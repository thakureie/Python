#/usr/bin/python
import re
def write_over():
    file_name = '/etc/sysctl.conf'
    new_string = 'net.ipv4.ipfrag_low_thresh = 15728640'

    fh = open(file_name, 'r+')
    data = fh.read()

    result = re.search("net.ipv4.ipfrag_low_thresh = 15728640", data) # check this regex, it may not be exactly what you need
    if result:
        if result.group(0) == new_string:  # if the string is exact match, do nothing
            fh.close()
            print("Already Matching")
        data = data.replace(result.group(0), new_string) # else replace with new string
        fh.truncate(0) # this will clear the contents of the file
        fh.write(data) # write the new data in its entirety to the file
        fh.close()
    else:
        fh.write('\n' + new_string) # if the line was not in the file at all
        fh.close()
