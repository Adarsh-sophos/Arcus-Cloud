#!/usr/bin/python2

import commands

def nfs_server(userName, driveSize, vgname, clientIP):
	
	"""
		folder at server-side --> /nfs-share/userName-lv1
	"""	
	
	#userName = raw_input ("Enter name of user: ")
	#driveSize = raw_input("Enter drive size: ")

	# 1. LV partition 2GB
	createPart = "lvcreate --size {0} --name {1}-lv1 {2}".format(driveSize, userName, vgname)
	driveCreateStatus = commands.getstatusoutput(createPart)

	if(driveCreateStatus[0] == 0):
		print("Drive created successfully...")
	
		# 2. format ext4
		formatF = commands.getstatusoutput("mkfs.ext4 /dev/{0}/{1}-lv1".format(vgname, userName))
		if(formatF[0] == 0):
			print("Formatted successfully.")
		else:
			print(formatF[1])
	
		# 3. mount folder /share
		commands.getstatusoutput("mkdir -p /nfs-share/{}-lv1". format(userName))
		mountF = commands.getstatusoutput("mount /dev/{0}/{1}-lv1 /nfs-share/{1}-lv1". format(vgname, userName))
		if(mountF[0] == 0):
			print("Drive mounted successfully.")
		else:
			print(mountF[1])
	
		#permanently mount
		fstabString = "/dev/{0}/{1}-lv1	/nfs-share/{1}-lv1 ext4 defaults 1 2\n\n". format(vgname, userName)
	
		# commands.getstatusoutput("echo '{}' >> /etc/fstab". format(fstabString))
	
		fstabfh = open('/etc/fstab', 'a')
		fstabfh.write(fstabString)
		fstabfh.close()

		fstabStatus = commands.getstatusoutput("mount -a")
		if(fstabStatus[0] == 0):
			pass
		else:
			print("There is some error in fstab, please check manually...")
			exit()
	
		# 4. NFS server: /etc/exports
		#    /share client_IP
		#clientIP = raw_input("Enter client IP, want to share: ")
		commands.getstatusoutput("echo '/nfs-share/{0}-lv1	{1}(rw,no_root_squash)' >> /etc/exports". format(userName, clientIP))
		commands.getstatusoutput("systemctl restart nfs")
		commands.getstatusoutput("systemctl stop firewalld")
		commands.getstatusoutput("setenforce 0")

	else:
		print("Drive not created.")
		print("Exiting...")
		exit()


	raw_input("Press enter to close...")



nfs_server('checking', '1G', 'vg1', '192.168.43.59')














