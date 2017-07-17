#!/usr/bin/python2
import commands,cgi

print "content-type: text/html"

stopRunning = commands.getstatusoutput('for container_id in $(docker ps  --filter="name=$name" -q -a);do docker stop $container_id;done')
if stopRunning[0]  == 0:
	print "location:  dp.py"
	print
else:
	print "Containers could not be stopped"
