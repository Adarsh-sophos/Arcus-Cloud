#!/usr/bin/python2

import config
import header
import cgi,commands,os,MySQLdb

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
	
	driveSize = cgi.FormContent()['driveSize'][0]
	clientIP = cgi.FormContent()['clientIP'][0]
	password = cgi.FormContent()['password'][0]
	vgname = 'vg1'
	
	lines = commands.getstatusoutput("sudo wc -l /Arcus/public/tmp/nfs/exports")
	
	sql = "INSERT INTO nfs(user_id,driveSize,clientIP,password,line,state) VALUES ({0},{1},'{2}','{3}',{4},'{5}')". format(int(header.cookie_value()), int(driveSize), clientIP, password, int(lines[1].split()[0])+1, 'm')
	try:
   		cursor.execute(sql)
	   	#db.commit()
	except:
	   	# Rollback in case there is any error
	   	print("could not insert in database")
	   	db.rollback()
	
	last_id = cursor.lastrowid
	
	exportsFp = open("/Arcus/public/tmp/nfs/exports", "a")
	exportsFp.write("/nfs-share/{0} {1}(rw,no_root_squash)\n". format(last_id, clientIP))
	exportsFp.close()

	ansibleString = """
#software install

- hosts: web

  tasks:

  - package:
      name: "nfs-utils"
      state: present


#create LV

  - lvol:
      vg: {3}
      lv: {0}
      size: {1}


#format LV

  - name: Format LV
    filesystem:
      fstype: ext4
      dev: /dev/{3}/{0}


#permanenly mount LV

  - name: Permanently mount LV
    mount:
      path: /nfs-share/{0}
      src: /dev/{3}/{0}
      fstype: ext4
      state: mounted

#echo '/nfs-share/{0}	{1}(rw,no_root_squash)' >> /etc/exports

  - name: "setup config file"
    copy:
      src: "/Arcus/public/tmp/nfs/exports"
      dest: "/etc/exports"

#systemctl restart nfs

  - service:
      name: "nfs"
      state: restarted
    """ .format(last_id, driveSize, clientIP, vgname)

	ansibleProg = open("/Arcus/public/tmp/nfs/nfs.ymal", "w")
	ansibleProg.write(ansibleString)
	ansibleProg.close()

	ansF = commands.getstatusoutput("sudo ansible-playbook /Arcus/public/tmp/nfs/nfs.ymal")
	
	if(ansF[0] == 0):

		# set up client
		dirF = commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sudo mkdir -p /media/{2}-{3}". format(password, clientIP, userName, last_id))
		mountF = commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sudo mount 192.168.43.171:/nfs-share/{3} /media/{2}-{3}". format(password, clientIP, userName, last_id))
	
		if(mountF[0] == 0):
			db.commit()
			print("Location:/activity.py\r\n\r\n")
		else:
			header.header_content()
			print(mountF[1])
			db.rollback()
		
	else:
		header.header_content()
		print("<pre> " + ansF[1] + " </pre>")
		db.rollback()
	

elif(os.environ['REQUEST_METHOD'] == "GET"):
	
	header.header_content()
	
	print """

    <div class="form-photo">
        <div class="form-container">
            <div class="image-holder" style="background-image:url(&quot;/img/svg_cloud_nfs.jpg&quot;);margin:10px;padding:20px;"></div>
            <form method="POST" action="nfs.py">
                <h2 class="text-center">NFS Share</h2>
                
                <div class="form-group">
                    <input class="form-control" type="text" name="driveSize" placeholder="Drive size in MB">
                </div>
                <div class="form-group">
                    <input class="form-control" type="text" name="clientIP" placeholder="Client IP">
                </div>
                <div class="form-group">
                    <input class="form-control" type="password" name="password" placeholder="Password">
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
    """

print """
    <script src="/js/jquery.min.js"></script>
    <script src="/bootstrap/js/bootstrap.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.15/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.15/js/dataTables.bootstrap.min.js"></script>
    <script src="/js/script.min.js"></script>
</body>

</html>
"""
