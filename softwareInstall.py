import commands

def softwareInstall(softwareName):

	webSoftware = commands.getstatusoutput("rpm -q {}". format(softwareName))

	if(webSoftware[0] == 0):
		print("{} already installed.". format(softwareName))
		
	else:
		print("{} is installing...". format(softwareName))
		webSoftwareInstalled = commands.getstatusoutput("yum install {} -y". format(softwareName))	
		if(webSoftwareInstalled[0] == 0):
			print("{} installed successfully.". format(softwareName))
		else:
			print("{} not installed.". format(softwareName))
