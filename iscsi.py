#!/usr/bin/python2

import config
import header
import cgi,commands,os,MySQLdb

header.header_content()

if(os.environ['REQUEST_METHOD'] == "POST"):
	
	db = MySQLdb.connect("localhost","root", "Aj1.....", "arcus")
	cursor = db.cursor()
	
	# get username
	sql = "SELECT * FROM users WHERE id={0}". format(header.cookie_value())
	try:
	   	cursor.execute(sql)
		results = cursor.fetchone()
		userName = results[1]
	except:
		print "Error: unable to fecth data"
	
	
	iqn = cgi.FormContent()['iqn'][0]
	vgname = 'vg1'
	clientIP = cgi.FormContent()['clientIP'][0]
	size = cgi.FormContent()['size'][0]
	
	sql = "INSERT INTO iscsi(user_id,size,clientIP,state,iqn) VALUES ({0},{1},'{2}','{3}','{4}')". format(int(header.cookie_value()), int(size), clientIP, "login", iqn)
	try:
   		cursor.execute(sql)
	   	#db.commit()
	except:
	   	# Rollback in case there is any error
	   	print("could not insert in database")
	   	db.rollback()
	
	last_id = cursor.lastrowid
	
	targetsFp = open("/Arcus/public/tmp/iscsi/targets.conf", "a")
	targetsFp.write("\n<target {0}>\n\tbacking-store /dev/{1}/{2}-iscsi\n</target>\n\n". format(iqn, vgname, last_id))
	targetsFp.close()

	ansibleString = """
- hosts: web

  tasks:

  #yum install scsi-target-utils -y
  - package:
      name: "scsi-target-utils"
      state: present

  #create LV
  - lvol:
      vg: {3}
      lv: {0}-iscsi
      size: {1}

  #create a partition in storage (don't format)

  #write in /etc/tgt/targets.conf file -
  #<target {2}>
  #	  backing-store /dev/{3}/{0}-iscsi
  #</target>
  
  - name: "setup config file"
    copy:
      src: "/Arcus/public/tmp/iscsi/targets.conf"
      dest: "/etc/tgt/targets.conf"

  #systemctl restart tgtd
  - service:
      name: "tgtd"
      state: restarted
""". format(last_id, size, iqn, vgname)

	ansibleProg = open("/Arcus/public/tmp/iscsi/iscsi.yaml", "w")
	ansibleProg.write(ansibleString)
	ansibleProg.close()

	ansF = commands.getstatusoutput("sudo ansible-playbook /Arcus/public/tmp/iscsi/iscsi.yaml")
	
	if(ansF[0] == 0):
		print("<pre> " + ansF[1] + " </pre>")
		
		# set up client
		sshString = "sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root  {1}". format("redhat", clientIP)
		
		inF = commands.getstatusoutput(sshString + " sudo yum install iscsi-initiator-utils -y")
		
		if(inF[0] == 0):
			disF = commands.getstatusoutput(sshString + " sudo iscsiadm --mode discoverydb --type sendtargets --portal {} --discover". format('192.168.43.171'))
			
			if(disF[0] == 0):			
				logF = commands.getstatusoutput(sshString + " sudo iscsiadm --mode node --targetname {0} --portal {1}:3260 --login". format(iqn, '192.168.43.171'))
				
				if(logF[0] == 0):
					print("<h3>setup complete</h3>")
					db.commit()
				else:
					print(logF[1])
					db.rollback()
			else:
				print(disF[1])
				db.rollback()
		else:
			print(inF[1])
			db.rollback()
	else:
		print("<pre> " + ansF[1] + " </pre>")
		db.rollback()
	
	
elif(os.environ['REQUEST_METHOD'] == "GET"):
	
	print """
	<div class="form-photo">
        <div class="form-container">
            <div class="image-holder" style="background-image:url(&quot;/img/svg_cloud_nfs.jpg&quot;);margin:10px;padding:20px;"></div>
            <form method="POST" action="iscsi.py">
                <h2 class="text-center">iSCSI Share</h2>
                <div class="form-group">
                    <input class="form-control" type="text" name="clientIP" placeholder="clientIP">
                </div>
                <div class="form-group">
                    <input class="form-control" type="text" name="size" placeholder="Drive size in MB">
                </div>
                <div class="form-group">
                    <input class="form-control" type="text" name="iqn" placeholder="IQN">
                </div>
                <div class="form-group has-success">
                    <div class="checkbox">
                        <label class="control-label" style="margin:auto;">
                            <input type="checkbox"> Confirm?</label>
                    </div>
                </div>
                <div class="form-group">
                    <button class="btn btn-primary btn-block" type="submit">SUBMIT </button>
                </div>
            </form>
        </div>
    </div>
    <script src="/js/jquery.min.js"></script>
    <script src="/bootstrap/js/bootstrap.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.15/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.15/js/dataTables.bootstrap.min.js"></script>
    <script src="/js/script.min.js"></script>
</body>

</html>
	"""
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
