#!/usr/bin/python2


import cgi
import commands

print "content-type: text/html"
#print

imageName=cgi.FormContent()['image'][0]
cName=cgi.FormContent()['cname'][0]
#chName=cgi.FormContent()['cbg']


containerStat=commands.getstatusoutput("sudo docker inspect {0}".format(cName))
if containerStat[0]  == 0:
	print "{} : this container name already exists".format(cName)

else:
	commands.getoutput("sudo docker run  -dit --name {0}  {1}".format(cName,imageName))
	#print "{}: Container launched ..".format(cName)
	print "Location: /dp.py\r\n\r\n"


"""
if imageName[0]=="ubuntu14.04":
	for i in chName:
		if chName[i]=="ssh":
			commands.getoutput("sudo apt-get install openssh-server")
		elif(chName[i] == 'apache'):
			commands.getoutput("sudo apt-get install apache2")
		elif(chName[i] ==  "nginx" ):
			commands.getoutput("sudo apt-get install nginx")
		elif(chName[i] == "htop" ):
			commands.getoutput("sudo apt-get install htop")
		
elif imageName[0]=="centos" or imageName[0]=="sshimg:v1":
	for i in chName:
		if chName[i]=="ssh":
			commands.getoutput("yum install openssh-server")
		elif(chName[i] == 'apache'):
			commands.getoutput("yum install httpd")
		elif(chName[i] ==  "nginx" ):
			commands.getoutput("yum install nginx")
		elif(chName[i] == "htop" ):
			commands.getoutput("yum install htop")
		



"""
