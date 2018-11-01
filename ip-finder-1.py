import os, sys

url = str(input("Please enter URL (FQDN) here : "))

def getipaddress(url):
  command = os.popen("host " + url )
  command1 = str(command.read())
  get1 = command1.find('has address') + 12
  return command1[get1:].splitlines()[0]

print(getipaddress(url))
