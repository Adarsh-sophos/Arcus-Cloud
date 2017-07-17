#!/usr/bin/python2

""" storage server IP need to be changed according to requirements in line number 94 """

import config
import header
import cgi,commands,os,MySQLdb

header.header_content()

if(os.environ['REQUEST_METHOD'] == "POST"):
	
	vgname = 'vg1'
	userName = cgi.FormContent()['userName'][0]
	driveSize = cgi.FormContent()['driveSize'][0]
	clientIP = cgi.FormContent()['clientIP'][0]
	password = cgi.FormContent()['userPass'][0]

	#step2: create lv

	ansibleLVCreate = """
- hosts : web

  tasks:

  - name: make a user
    command: sudo useradd {0}
  
  - name: set password
    command: echo "redhat" | passwd {0} --stdin

  #- name: make a user
  #  user:
  #    name: {0}
  #    password: {3}

  - name: make directory
    file:
      state: directory
      path: /sshfs/{0}-lv1

  # change owner of shared folder
  - name: changing owner to {0}
    command: sudo chown -R {0} /sshfs/{0}-lv1/
   
  - name: give all permissions to user {0}
    command: sudo chmod 700 /sshfs/{0}-lv1

  - name: creating lv from vg
    lvol:
      lv: {0}-lv1
      vg: {2}
      size: {1}

  # formating the created lv
  - name: Format LV
    filesystem:
      fstype: ext4
      dev: /dev/{2}/{0}-lv1

  # mount the lv permanently
  - name: permanent mount lv
    mount:
      path: /sshfs/{0}-lv1
      src: /dev/{2}/{0}-lv1
      fstype: ext4
      state: mounted

  # restart ssh
  - service:
      name: "sshd"
      state: restarted """. format(userName, driveSize, vgname, password)


	sshfsProg = open("/Arcus/public/tmp/sshfs/sshfs.yaml", "w")
	sshfsProg.write(ansibleLVCreate)
	sshfsProg.close()

	ansF= commands.getstatusoutput("sudo ansible-playbook /Arcus/public/tmp/sshfs/sshfs.yaml")
	print("<pre>"+ ansF[1]+ "</pre>")
	
	# set up client
	commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root  {1}  mkdir /storage/emulated/{2}/".format(password,clientIP,userName))

	'''sshpassF = commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root  {1}  yum install sshpass -y".format(password,clientIP))
	if(sshpassF[0]==0):
		print("sshpass installed")
	else:
		print(sshpassF[1])'''

	'''sshfsF = commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root  {1}  yum install fuse-sshfs -y".format(password,clientIP))
	if sshfsF[0]==0:
		print("sshfs installed")
	else:
		print(sshfsF[1])'''

	mountF = commands.getstatusoutput("sudo sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} sshfs -o stricthostkeychecking=no {2}@192.168.43.171:/sshfs/{2}-lv1 /storage/emulated/{2}/".format(password,clientIP,userName))
	if(mountF[0] == 0):
		print("successfully mounted")
	else:
		print(mountF[1])
		
	

elif(os.environ['REQUEST_METHOD'] == "GET"):
	
	print """
	
	<form action="/sshfs.py" method="POST">
		user name: <input type="text" name="userName" />	<br/>
		drive size: <input type="text" name="driveSize" />	<br/>
		IP Address: <input type="text" name="clientIP" />	<br/>
		Password: <input type="password" name="userPass" />	<br/>
		<button type="submit">Get</button>
	</form>
	"""
	
	"""
	<div class="register-photo">
        <div class="form-container">
            <div class="image-holder" style="background-image:url(&quot;assets/img/svg_cloud_nfs.jpg&quot;);margin:10px;padding:20px;"></div>
            <form method="post">
                <h2 class="text-center">SSHFS SHARE</h2>
                <div class="form-group">
                    <input class="form-control" type="text" name="userName" placeholder="username">
                </div>
                <div class="table-responsive">
    <table class="table"><tr>
    <td>
        <input type="range" style="  height:40px;
  width:130px;
" min="8" step="1" max="2048" for="osDRIVEsize" name="osDRIVE" />
    </td>
    <td>
        <input style="  width:110px;
" type="number" placeholder="Drive Size" class="form-control" min="8" step="1" max="2048" for="osDRIVE" name="osDRIVEsize" />
    </td>
    <td> <span class="input-group-addon" style="  height:40px;
">GB</span></td>
</tr>

</table>
</div>
                <div class="form-group"></div>
                <input class="form-control" type="text" name="clientIP" placeholder="Client IP">
                <div class="form-group"></div>
                <input class="form-control" type="text" name="clientIP" placeholder="Password">
                <div class="form-group"></div>
                <div class="form-group"></div>
                <div class="form-group"></div>
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
	
	
	
	
	
	
	
	
	
	
