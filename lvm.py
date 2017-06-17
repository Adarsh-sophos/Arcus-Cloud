import sys,os
from commands import getstatusoutput


def make_PV(driveNames):

	# create PV of every partition
	for drive in driveNames:
		PV = "pvcreate {}".format(drive)
		driveF = getstatusoutput(PV)
	
		if(driveF[0] == 0):
			print(driveF[1])
		else:
			print(driveF[1])
			

def make_VG(driveNames, vgname):
	
	# make VG from created PVs	
	VG = "vgcreate "+ vgname + " "
	for drive in driveNames:
		VG = VG + drive + " "

	vgF = getstatusoutput(VG)
	if(vgF[0] == 0):
		print(vgF[1])
	else:
		print(vgF[1])
		

def make_LV(lvname, lvsize, vgname):

	# make LV from created VG
	LV = "lvcreate --size {0} --name {1} {2}". format(lvsize, lvname, vgname)
	lvF = getstatusoutput(LV)

	if(lvF[0] == 0):
		print(lvF[1])
	else:
		print(lvF[1])
		

def remove_PV(driveNames):

	# Remove PV of every partition
	for drive in driveNames:
		PV = "pvremove {}". format(drive)
		driveF = getstatusoutput(PV)
	
		if(driveF[0] == 0):
			print(driveF[1])
		else:
			print(driveF[1])
			

def remove_VG(vgname):
	
	# remove VG
	VG = "vgremove "+ vgname
	vgF = getstatusoutput(VG)
	
	if(vgF[0] == 0):
		print(vgF[1])
	else:
		print(vgF[1])
		


def remove_LV(lvname):

	# remove LV
	LV = "echo y | lvremove " + lvname
	lvF = getstatusoutput(LV)

	if(lvF[0] == 0):
		print(lvF[1])
	else:
		print(lvF[1])


def display_PV(driveName):

	# Display PV
	PV = "pvdisplay {}". format(driveName)
	driveF = getstatusoutput(PV)
	
	if(driveF[0] == 0):
		print(driveF[1])
	else:
		print(driveF[1])
			

def display_VG(vgname):
	
	# Display VG
	VG = "vgdisplay "+ vgname
	vgF = getstatusoutput(VG)
	
	if(vgF[0] == 0):
		print(vgF[1])
	else:
		print(vgF[1])
		


def display_LV(lvname):

	# Display LV 
	LV = "lvdisplay " + lvname
	lvF = getstatusoutput(LV)

	if(lvF[0] == 0):
		print(lvF[1])
	else:
		print(lvF[1])


def extend_VG(driveName, vgname):
	
	VG = "vgextend {0} {1}". format(vgname, driveName)
	vgF = getstatusoutput(VG)
	
	if(vgF[0] == 0):
		print(vgF[1])
	else:
		print(vgF[1])


def reduce_VG(driveName, vgname):
	
	VG = "vgreduce {0} {1}". format(vgname, driveName)
	vgF = getstatusoutput(VG)
	
	if(vgF[0] == 0):
		print(vgF[1])
	else:
		print(vgF[1])		


def format_LV(lvpath, formatType):
	
	fLV = "mkfs.{0} {1}". format(formatType, lvpath)
	lvF = getstatusoutput(fLV)
	
	if(lvF[0] == 0):
		print(lvF[1])
	else:
		print(lvF[1])


def extend_LV(lvpath, lvsize):
	
	extendLV = "lvextend --size +{0} {1}". format(lvsize, lvpath)
	lvF = getstatusoutput(extendLV)
	
	if(lvF[0] == 0):
		print(lvF[1])
	else:
		print(lvF[1])


def reduce_LV(lvpath, lvsize):
	
	reduceLV = "echo y | lvreduce --size -{0} {1}". format(lvsize, lvpath)
	lvF = getstatusoutput(reduceLV)
	
	if(lvF[0] == 0):
		print(lvF[1])
	else:
		print(lvF[1])


def format_extended_LV(lvpath):
	
	fLV = "resize2fs " + lvpath
	lvF = getstatusoutput(fLV)
	
	if(lvF[0] == 0):
		print(lvF[1])
	else:
		print(lvF[1])


os.system('tput setaf 1')
print("\t\t\t\twelcome to my menu !!")
os.system('tput setaf 7')
print("\t\t\t\t---------------------")

while(1):

	print """
	press      1     : To create everything (PV, VG, LV))
	press (2a,2b,2c) : To create (a)PVs / (b)VG / (c)LV
	press (3a,3b,3c) : To remove (a)PVs / (b)VG / (c)LV
	press (4a,4b,4c) : To display (a)PV / (b)VG / (c)LV
	press   (5a,5b)  : To (a)extend (b)reduce VG size
	press   (6a,6b)  : To (a)extend (b)reduce LV size
	press   (7a,7b)  : To format (a)LV (b)extended LV
	press      8     : to exit
	"""

	ch = raw_input("Enter your choice: ")
	
	if(ch == '1'):
		# input drive names
		driveNames = raw_input("Enter Drive Names (full path) to create PV separated by space: ").split()
		make_PV(driveNames)

		# input VG name
		vgname = raw_input("Enter Volume Group (VG) name: ")
		make_VG(driveNames, vgname)

		# input LV name and size
		lvname = raw_input("Enter Logical Volume (LV) name: ")
		lvsize = raw_input("Enter Logical Volume (LV) size: ")
		make_LV(lvname, lvsize, vgname)
		
		# format LV
		formatType = raw_input("Enter format type: ")
		format_LV('/dev/'+vgname+'/'+lvname, formatType)
	
		
	elif(ch == '2a'):
		driveNames = raw_input("Enter Drive Names (full path) to create VG separated by space: ").split()
		make_PV(driveNames)

	elif(ch == '2b'):
		driveNames = raw_input("Enter Drive Names (full path) to create VG separated by space: ").split()
		vgname = raw_input("Enter Volume Group (VG) name: ")
		make_VG(driveNames, vgname)
		
	elif(ch == '2c'):		
		lvname = raw_input("Enter Logical Volume (LV) name: ")
		lvsize = raw_input("Enter Logical Volume (LV) size: ")
		vgname = raw_input("Enter Volume Group (VG) name: ")
		make_LV(lvname, lvsize, vgname)

	
	
	elif(ch == '3a'):
		driveNames = raw_input("Enter Drive Names (full path) to remove PV separated by space: ").split()
		remove_PV(driveNames)
	
	elif(ch == '3b'):
		vgname = raw_input("Enter Volume Group (VG) name: ")
		remove_VG(vgname)
		
	elif(ch == '3c'):
		lvname = raw_input("Enter Logical Volume (LV) name: ")
		remove_LV(lvname)

		
	elif(ch == '4a'):
		driveNames = raw_input("Enter Drive Name (full path): ")
		display_PV(driveNames)
		
	elif(ch == '4b'):
		vgname = raw_input("Enter Volume Group (VG) name: ")
		display_VG(vgname)
		
	elif(ch == '4c'):
		lvpath = raw_input("Enter Logical Volume (LV) path: ")
		display_LV(lvpath)
	
	elif(ch == '5a'):
		vgname = raw_input("Enter Volume Group (VG) name: ")
		driveName = raw_input("Enter drive name (full path) to be extended: ")		
		extend_VG(driveName, vgname)
		
	elif(ch == '5b'):
		vgname = raw_input("Enter Volume Group (VG) name: ")
		driveName = raw_input("Enter drive name (full path) to be reduced: ")		
		reduce_VG(driveName, vgname)
	
	elif(ch == '6a'):
		lvpath = raw_input("Enter Logical Volume (LV) path: ")
		lvsize = raw_input("Enter size to be extended in LV: ")
		extend_LV(lvpath, lvsize)
		
	elif(ch == '6b'):
		lvpath = raw_input("Enter Logical Volume (LV) path: ")
		lvsize = raw_input("Enter size to be reduced from LV: ")
		reduce_LV(lvpath, lvsize)
	
	elif(ch == '7a'):
		# format LV
		lvpath = raw_input("Enter LV path to be formatted: ")
		formatType = raw_input("Enter format type: ")
		format_LV(lvpath, formatType)
	
	elif(ch == '7b'):
		# format extended LV
		lvpath = raw_input("Enter LV path to be formatted: ")
		format_extended_LV(lvpath)
	
	elif(ch == '8'):
		sys.exit(0)
	
	os.system('tput setaf 6')
	raw_input("Press Enter to continue...")
	os.system('tput setaf 7')
	os.system("clear")
		




















