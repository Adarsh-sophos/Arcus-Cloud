#!/usr/bin/python2
import commands,cgi

print "content-type: text/html"

remStopped = commands.getstatusoutput("for container_id in $(docker ps  --filter="name=$name" -q -a);do docker rm $container_id;done")
if remStopped[0]  == 0:
	print "location:  dp.py"
	print
else:
	print "Container could not be removed"
