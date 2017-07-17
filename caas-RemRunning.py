#!/usr/bin/python2
import commands,cgi

print "content-type: text/html"

remRunning = commands.getstatusoutput('for container_id in $(docker ps  --filter="name=$name" -q);do docker stop $container_id && docker rm $container_id;done')
if remRunning[0]  == 0:
	print "location:  dp.py"
	print
else:
	print "Containers could not be removed"
