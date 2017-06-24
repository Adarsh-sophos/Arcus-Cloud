#!/usr/bin/python2

import commands

userName = raw_input("Enter user name: ")
driveName = raw_input("Enter your drive name: ")
mountPointCreator = commands.getstatusoutput("mkdir -p /media/{}". format(driveName))

if(mountPointCreator[0] == 0):
	print("directory {} is created.". format(driveName))
else:
	print("Cannot create directory {}". format(driveName))

serverIP = raw_input("Enter server IP: ")
shareMount = commands.getstatusoutput("mount {0}:/nfs-share/{1}-lv1 /media/{2}". format(serverIP, userName , driveName))

if(shareMount[0] == 0):
	print("Drive created")
	
	while(True):
		removeDrive = raw_input("Press 'q' to unmount '{}': ". format(driveName))
		if(removeDrive == "q"):
			commands.getstatusoutput("umount /media/{}". format(driveName))
			raw_input("Successfully removed.\nPress enter to close...")
			break
		else:
			print ("Option not supported")
else:
	print ("Drive not created...")


