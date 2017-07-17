#!/usr/bin/python2

import header
import cgi
import commands

header.header_content()

osDistro=cgi.FormContent()['OSName'][0]
ostype= "linux"
osname=cgi.FormContent()['OSLabel'][0]
cpunumber=cgi.FormContent()['CPUCores'][0]
ramsize=cgi.FormContent()['osRAM'][0]
storagesize=cgi.FormContent()['osDRIVE'][0]
hypervisorIP=cgi.FormContent()['hypervIP'][0]

if osDistro == "1":
	distro="rhel-server-7.3-x86_64-dvd.iso"
	osVariant = "rhel7"
elif osDistro == "2":
	distro="ubuntu-16.04-desktop-amd64.iso"
	osVariant = "ubuntu16.04"
elif osDistro == "3":
	distro="Fedora-Live-Workstation-x86_64-23-10.iso"
	osVariant = "fedora23"
elif osDistro == "4":
	distro="archlinux-2017.05.01-x86_64.iso"
	osVariant = "archlinux"
else: 
	distro = "Null"
	osVariant = ""

ossetup="sudo sshpass -p redhat ssh -o stricthostkeychecking=no -l root 192.168.43.14 virt-install --name  {0} --location  /images/{5}  --os-type linux  --os-variant {6} --memory  {4} --vcpus  {2} --disk  /dev/sdb1/{0}.qcow2,size={3} --graphics  vnc,listen=0.0.0.0,port=5901  --noautoconsole".format(osVariant,ostype,cpunumber,storagesize,ramsize,distro,osVariant)

ossetupstatus=commands.getstatusoutput(ossetup)

if ossetupstatus[0] == 0:
	print "<h1>done!</h1>"
	
else:
	print ("Error:" + ossetupstatus[1])
	







