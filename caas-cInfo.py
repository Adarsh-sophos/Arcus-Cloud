#!/usr/bin/python2
import commands,cgi

print "content-type: text/html"

containerName = cgi.FormContent()['containerName'][0]
cInfoStatus = commands.getstatusoutput("sudo docker rm -f {}".format(containerName))
if cRemoveStatus[0]  == 0:
	print "location:  dp.py"
	print
else:
	print "not removed"