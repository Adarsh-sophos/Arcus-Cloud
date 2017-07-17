#!/usr/bin/python2
import commands,cgi

print "content-type: text/html"

containerName = cgi.FormContent()['containerName'][0]
state = cgi.FormContent()['cStatus'][0]

if state == "pause":
	cPauseStatus = commands.getstatusoutput("sudo docker pause {}".format(containerName))
	if cPauseStatus[0]  == 0:
		print "location:  dp.py"
		print
	else:
		print "Container could not be paused"
elif state == "unpause":
	cPauseStatus = commands.getstatusoutput("sudo docker unpause {}".format(containerName))
	if cPauseStatus[0]  == 0:
		print "location:  dp.py"
		print
	else:
		print "Container could not be unpaused"
else:
	cPauseStatus = commands.getstatusoutput("sudo docker unpause {}".format(containerName))
	if cPauseStatus[0]  == 0:
		print "location:  dp.py"
		print
	else:
		print "Container could not be unpaused"








