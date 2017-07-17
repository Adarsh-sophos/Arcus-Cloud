#!/usr/bin/python2
import commands,cgi

print "content-type: text/html"

containerName = cgi.FormContent()['containerName'][0]
cStopStatus = commands.getstatusoutput("sudo docker start {}".format(containerName))
if cStopStatus[0]  == 0:
	print "location:  dp.py"
	print
else:
	print "Container could not be stopped"









