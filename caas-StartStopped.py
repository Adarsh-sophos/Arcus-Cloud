#!/usr/bin/python2
import commands,cgi

print "content-type: text/html"

startStopped = commands.getstatusoutput('for container_id in $(docker ps  --filter="name=$name" -q -a);do docker start -dit $container_id;done')
if startStopped[0]  == 0:
	print "location:  dp.py"
	print
else:
	print "Containers could not be stopped"

