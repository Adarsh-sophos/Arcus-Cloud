#!/usr/bin/python2

import config
import header
import cgi,commands,os,MySQLdb
import datetime


def remove(nfs_id):
	
	removeString = """
- hosts: web
  tasks:
  
  - command: sudo umount -l /nfs-share/{0}
  
  - lvol:
      vg: vg1
      lv: {0}
      state: absent
      force: yes """. format(nfs_id)

	ansibleProg = open("/Arcus/public/tmp/nfs/remove.yaml", "w")
	ansibleProg.write(removeString)
	ansibleProg.close()

	ansF = commands.getstatusoutput("sudo ansible-playbook /Arcus/public/tmp/nfs/remove.yaml")
	
	if(ansF[0] == 0):
		
		mountF = commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sudo rm -rf /nfs-share/{2}". format("redhat", "192.168.43.171", nfs_id))
		
		sql = "DELETE FROM nfs WHERE id={0}". format(nfs_id)
		try:
	   		cursor.execute(sql)
		   	db.commit()
		   	print("Location:/activity.py\r\n\r\n")
		except:
			header.header_content()
		   	print("can not delete entry")
		   	db.rollback()
	else:
		header.header_content()
		print("<pre> " + ansF[1] + " </pre>")
	


db = MySQLdb.connect("localhost","root", "Aj1.....", "arcus")
cursor = db.cursor()

service = cgi.FormContent()['service'][0]
stype = cgi.FormContent()['type'][0]
user_id = header.cookie_value()

# get username
sql = "SELECT * FROM users WHERE id={0}". format(user_id)
try:
   	cursor.execute(sql)
	results = cursor.fetchone()
	userName = results[1]
except:
	print "Error: unable to fecth data"


if(stype == "nfs"):
	
	nfs_id = cgi.FormContent()['id'][0]
	# get nfs storage information
	sql = "SELECT * FROM nfs WHERE id={0}". format(nfs_id)
	try:
	   	cursor.execute(sql)
		results = cursor.fetchone()
	except:
		print "Error: unable to fecth data"

elif(stype == "iscsi"):
	
	iscsi_id = cgi.FormContent()['id'][0]
	# get nfs storage information
	sql = "SELECT * FROM iscsi WHERE id={0}". format(iscsi_id)
	try:
	   	cursor.execute(sql)
		results = cursor.fetchone()
	except:
		print "Error: unable to fecth data"
		
# get current drive size
currentSize = results[2]


if(service == "extend"):
	extendSize = cgi.FormContent()['extendSize'][0]
	
	if(stype=="nfs"):
		extendString = """
- hosts: web
  tasks:
  - lvol:
      vg: vg1
      lv: {0}
      size: {1}

  - name: resizing fs
    command: resize2fs /dev/vg1/{0}
      
      	""". format(results[0], currentSize+int(extendSize))

	elif(stype=="iscsi"):
		extendString = """
- hosts: web
  tasks:
  - lvol:
      vg: vg1
      lv: {0}-iscsi
      size: {1}

  - name: resizing fs
    command: resize2fs /dev/vg1/{0}-iscsi
      
      	""". format(results[0], currentSize+int(extendSize))

	ansibleProg = open("/Arcus/public/tmp/nfs/extend.yaml", "w")
	ansibleProg.write(extendString)
	ansibleProg.close()

	ansF = commands.getstatusoutput("sudo ansible-playbook /Arcus/public/tmp/nfs/extend.yaml")
	
	if(ansF[0] == 0):
		if(stype=="nfs"):
			sql = "UPDATE nfs SET driveSize={0} WHERE id={1}". format(currentSize+int(extendSize), nfs_id)
		elif(stype=="nfs"):
			sql = "UPDATE iscsi SET size={0} WHERE id={1}". format(currentSize+int(extendSize), iscsi_id)
			
		try:
	   		cursor.execute(sql)
		   	db.commit()
		   	print("Location:/activity.py\r\n\r\n")
		except:
			header.header_content()
		   	print("can not update database")
		   	db.rollback()
	else:
		header.header_content()
		print("<pre> " + ansF[1] + " </pre>")


elif(service == "remove"):
	
	# unmount from client side
	if(results[6] == 'm'):
		mountF = commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sudo umount /media/{2}-{3}". format(results[4], results[3], userName, results[0]))
		
		sql = "UPDATE nfs SET state='u' WHERE id={0}". format(nfs_id)
		try:
			cursor.execute(sql)
		   	db.commit()
		   	
		except:
			header.header_content()
		   	print("can not update database")
		   	db.rollback()
		
		mountF = commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sudo rm -rf /media/{2}-{3}". format(results[4], results[3], userName, results[0]))
		
		remove(results[0])
	
	else:
		mountF = commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sudo rm -rf /media/{2}-{3}". format(results[4], results[3], userName, results[0]))
		
		remove(results[0])
	
	

elif(service == "unmount"):
	
	# unmount from client side
	mountF = commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sudo umount /media/{2}-{3}". format(results[4], results[3], userName, results[0]))
	
	if(mountF[0] == 0):
		sql = "UPDATE nfs SET state='u' WHERE id={0}". format(nfs_id)
		try:
			cursor.execute(sql)
		   	db.commit()
		   	print("Location:/activity.py\r\n\r\n")
		except:
			header.header_content()
		   	print("can not update database")
		   	db.rollback()		
		
	else:
		header.header_content()
		print(mountF[1])


elif(service == "mount"):
	
	dirF = commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sudo mkdir -p /media/{2}-{3}". format(results[4], results[3], userName, results[0]))
	mountF = commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sudo mount 192.168.43.171:/nfs-share/{3} /media/{2}-{3}". format(results[4], results[3], userName, results[0]))
	
	if(mountF[0] == 0):
		sql = "UPDATE nfs SET state='m' WHERE id={0}". format(nfs_id)
		try:
			cursor.execute(sql)
		   	db.commit()
		   	print("Location:/activity.py\r\n\r\n")
		except:
			header.header_content()
		   	print("can not update database")
		   	db.rollback()		
		
	else:
		header.header_content()
		print(mountF[1])

	
elif(service == "snapshot"):
	
	if(stype == "nfs"):
		snapName = datetime.datetime.now().strftime('%d-%h-%Y-%H-%M-%S')
		snapString = """
- hosts: web
  tasks:
  
  - lvol:
      vg: vg1
      lv: {1}
      size: {0}
      snapshot: {2} """. format(currentSize, nfs_id, snapName)
     
	elif(stype == "iscsi"):
		snapName = datetime.datetime.now().strftime('%d-%h-%Y-%H-%M-%S')
		snapString = """
- hosts: web
  tasks:
  
  - lvol:
      vg: vg1
      lv: {1}-iscsi
      size: {0}
      snapshot: {2} """. format(currentSize, iscsi_id, snapName)

	ansibleProg = open("/Arcus/public/tmp/nfs/snapshot.yaml", "w")
	ansibleProg.write(snapString)
	ansibleProg.close()

	ansF = commands.getstatusoutput("sudo ansible-playbook /Arcus/public/tmp/nfs/snapshot.yaml")
	
	if(ansF[0] == 0):

		#"lvcreate --size {0} --name {2} -s /dev/vg1/{1}""". format(current_size, nfs_id, snapName)
		if(stype == "nfs"):
			sql = "INSERT INTO snapshot(nfs_id, snap_name) VALUES ({0},'{1}')". format(nfs_id, snapName)
		elif(stype == "iscsi"):
			sql = "INSERT INTO snapshot_iscsi(iscsi_id, snap_name) VALUES ({0},'{1}')". format(iscsi_id, snapName)

		try:
		   	cursor.execute(sql)
			db.commit()
			print("Location:/activity.py\r\n\r\n")
		except:
			header.header_content()
			print "Error: unable to insert data"
			db.rollback()
	else:
		header.header_content()
		print("<pre> " + ansF[1] + " </pre>")
	


elif(service == "login"):

	sshString = "sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root  {1}". format("redhat", results[3])
	
	disF = commands.getstatusoutput(sshString + " sudo iscsiadm --mode discoverydb --type sendtargets --portal {} --discover". format('192.168.43.171'))

	if(disF[0] == 0):
		logF = commands.getstatusoutput(sshString + " sudo iscsiadm --mode node --targetname {0} --portal {1}:3260 --login". format(results[5], '192.168.43.171'))
			
		if(logF[0] == 0):			
			sql = "UPDATE iscsi SET state='login' WHERE id={0}". format(iscsi_id)
			try:
				cursor.execute(sql)
			   	db.commit()
			   	print("Location:/activity.py\r\n\r\n")
			except:
				header.header_content()
			   	print("can not update database")
			   	db.rollback()	
		else:
			header.header_content()
			print(logF[1])
	else:
		header.header_content()
		print(disF[1])
		

elif(service == "logout"):
	
	sshString = "sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root  {1}". format("redhat", results[3])
	
	logF = commands.getstatusoutput(sshString + " sudo iscsiadm --mode node --targetname {0} --portal {1}:3260 --logout". format(results[5], '192.168.43.171'))
		
	if(logF[0] == 0):			
		sql = "UPDATE iscsi SET state='logout' WHERE id={0}". format(iscsi_id)
		try:
			cursor.execute(sql)
		   	db.commit()
		   	print("Location:/activity.py\r\n\r\n")
		except:
			header.header_content()
		   	print("can not update database")
		   	db.rollback()	
	else:
		header.header_content()
		print(logF[1])


	
print """
    <script src="/js/jquery.min.js"></script>
    <script src="/bootstrap/js/bootstrap.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.15/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.15/js/dataTables.bootstrap.min.js"></script>
    <script src="/js/script.min.js"></script>
</body>

</html>
"""
	
	
	
	
	
	

