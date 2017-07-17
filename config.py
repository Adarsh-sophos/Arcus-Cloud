#!/usr/bin/python2

import MySQLdb,Cookie,os

db = MySQLdb.connect("localhost","root", "Aj1.....", "arcus")
cursor = db.cursor()

if(not os.environ['SCRIPT_NAME'] in  ["/login.py", "/logout.py", "/index.py"]):
	
	if('HTTP_COOKIE' in os.environ):
		cookie_string = os.environ.get('HTTP_COOKIE')
		c = Cookie.SimpleCookie()
		c.load(cookie_string)

		try:
		    data=c['id'].value
		    print "cookie data: "+data+"<br>"
		except KeyError:
		    print("Location:/login.py\r\n\r\n")
	else:
		print("Location:/login.py\r\n\r\n")


elif(os.environ['SCRIPT_NAME'] == "/login.py"):
	if('HTTP_COOKIE' in os.environ):
		cookie_string = os.environ.get('HTTP_COOKIE')
		c = Cookie.SimpleCookie()
		c.load(cookie_string)

		try:
		    data=c['id'].value
		    print("Location:/\r\n\r\n")
		except KeyError:
		    print("")
	else:
		pass
