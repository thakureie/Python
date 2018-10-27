#!/usr/bin/python
#wraps up rsync to synchronize two directories
from subprocess import call
import sys

source = "/tmp/sync_dirA"/  #Note the trailing slash
target = "/tmp/sync_dirB"
rsync = "rsync"
argument = "-a"
cmd = "%s %s %s " % (rsync, arguments, source, target)

def sync():

ret = call(cmd, shell=True)
if ret !=0:
print("rsync failed")
sys.exit(1)
sync()
