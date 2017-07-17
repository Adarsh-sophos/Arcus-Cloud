#!/usr/bin/python2

import config
import header
import cgi,commands,os,MySQLdb
import cgitb; cgitb.enable()



if(os.environ['REQUEST_METHOD'] == "POST"):
	# commands.getstatusoutput("sudo docker run -dit --name mysql-demo -e MYSQL_ROOT_PASSWORD={0} mysql:latest". format(password))
	
	# change /etc/phpMyAdmin/config.inc.php
	
	print("Location:http://192.168.43.59/phpmyadmin\r\n\r\n")
	

elif(os.environ['REQUEST_METHOD'] == "GET"):
	header.header_content()
	print """
<div class="form-photo">
      <div class="form-container">
	<h3> Use MySQL Database </h3>
	<form action="/dbaas.py" method="POST">
		<div class="form-group">
                    <input class="form-control" type="password" name="password" placeholder="Enter Password">
                </div>
		<div class="form-group">
                    <button class="btn btn-primary btn-block" type="submit">SET-UP </button>
                </div>
	</form> 
</div>
</div> """
