'''
SERVER -->

yum install scsi-target-utils -y

create a partition in storage (don't format)

write in /etc/tgt/targets.conf file -
<target IQN>
	backing-store partiton_path
</target>

systemctl restart tgtd

tgt-admin -show
'''

'''
CLIENT -->

yum install iscsi-initiator-utils

discover
iscsiadm --mode discoverydb --type sendtargets --portal cloud_IP --discover

login
iscsiadm --mode node --targetname IQN -portal cloud_IP:3260 --login

logout
iscsiadm --mode node --targetname IQN -portal cloud_IP:3260 --logout
'''

from softwareInstall import softwareInstall
from commands import getstatusoutput


print """
	press 1 : setup iSCSI server
	press 2 : setup iSCSI client
"""

ch = int(raw_input("Enter your choice: "))

if(ch == 1):
	
	#install software
	softwareInstall('scsi-target-utils')
	
	iqn = raw_input("Enter IQN: ")
	driveName = raw_input("Enter partition path for client: ")
	
	#configure
	fp = open("/etc/tgt/targets.conf", "w")
	fp.write('# This is a sample config file for tgt-admin.\n#\n# The "#" symbol disables the processing of a line.\n\n# Set the driver. If not specified, defaults to "iscsi".\ndefault-driver iscsi\n\n')
	fp.write("<target {}>\n". format(iqn))
	fp.write("\tbacking-store {}\n". format(driveName))
	fp.write("</target>\n\n")
	fp.write('# Set iSNS parameters, if needed\n#iSNSServerIP 192.168.111.222\n#iSNSServerPort 3205\n#iSNSAccessControl On\n#iSNS On\n\n# Continue if tgtadm exits with non-zero code (equivalent of\n# --ignore-errors command line option)\n#ignore-errors yes')
	fp.close()
	
	#start service
	print("Starting iSCSI server...")
	serviceF = getstatusoutput("systemctl restart tgtd")
	if(serviceF[0] == 0):
		print("iSCSI server started.")
	else:
		print(serviceF[1])


elif(ch == 2):
	
	#install software
	print("Installing software...")
	softwareInstall("iscsi-initiator-utils")
	
	iqn = raw_input("Enter IQN: ")
	cloudIP = raw_input("Enter cloud system IP: ")
	
	#discovery command
	discoveryF = getstatusoutput("iscsiadm --mode discoverydb --type sendtargets --portal {} --discover". format(cloudIP))
	if(discoveryF[0] == 0):
		if(discoveryF[1].split()[1] == iqn):
			print("Discovered {0} on cloud {1}". format(iqn, cloudIP))
		else:
			print("Cannot discover {0} on cloud IP {1}". format(iqn, cloudIP))
			print("Exiting...")
			exit()
	else:
		print(discoverF[1])

	#login request
	loginF = getstatusoutput("iscsiadm --mode node --targetname {0} --portal {1}:3260 --login". format(iqn, cloudIP))
	if(loginF[0] == 0):
		print(loginF[1])
	else:
		print(loginF[1])
		print("Exiting...")
		exit()

	#logout request
	raw_input("Press l for logout: ")
	logoutF = getstatusoutput("iscsiadm --mode node --targetname {0} --portal {1}:3260 --logout". format(iqn, cloudIP))
	print(logoutF[1])












