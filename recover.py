#!/usr/bin/python2

import config
import header
import cgi,commands,os,MySQLdb



db = MySQLdb.connect("localhost","root", "Aj1.....", "arcus")
cursor = db.cursor()

user_id = header.cookie_value()

# get username
sql = "SELECT * FROM users WHERE id={0}". format(user_id)
try:
   	cursor.execute(sql)
	results = cursor.fetchone()
	userName = results[1]
except:
	print "Error: unable to fecth data"


snap_name = cgi.FormContent()['n'][0]
nfs_id = cgi.FormContent()['id'][0]

# get nfs storage information
sql = "SELECT * FROM nfs WHERE id={0}". format(nfs_id)
try:
   	cursor.execute(sql)
	results = cursor.fetchone()
except:
	print "Error: unable to fecth data"



exportsFp = open("/Arcus/public/tmp/nfs/exports", "a")
exportsFp.write("/nfs-share/recover-{0} {1}(rw,no_root_squash)\n". format(nfs_id, results[3]))
exportsFp.close()

ansibleString = """
#software install

- hosts: web

  tasks:

  - package:
      name: "nfs-utils"
      state: present

  - name: Permanently mount LV
    mount:
      path: /nfs-share/recover-{0}
      src: /dev/vg1/{1}
      fstype: ext4
      state: mounted

  - name: "setup config file"
    copy:
      src: "/Arcus/public/tmp/nfs/exports"
      dest: "/etc/exports"

#systemctl restart nfs

  - service:
      name: "nfs"
      state: restarted
""". format(nfs_id, snap_name)

ansibleProg = open("/Arcus/public/tmp/nfs/nfs.ymal", "w")
ansibleProg.write(ansibleString)
ansibleProg.close()

ansF = commands.getstatusoutput("sudo ansible-playbook /Arcus/public/tmp/nfs/nfs.ymal")
	
if(ansF[0] == 0):

	# set up client
	dirF = commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sudo mkdir -p /media/recover-{2}". format(results[4], results[3], nfs_id))
	mountF = commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sudo mount 192.168.43.171:/nfs-share/recover-{2} /media/recover-{2}". format(results[4], results[3], nfs_id))
	
	if(mountF[0] == 0):
		header.header_content()
		print("<h2> Successfully Recovered</h2>")
	else:
		header.header_content()
		print(mountF[1])
		
else:
	header.header_content()
	print("<pre> " + ansF[1] + " </pre>")
	
