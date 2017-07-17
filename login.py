#!/usr/bin/python2

import config
import header
import cgi,commands,os,MySQLdb
import Cookie

db = MySQLdb.connect("localhost","root", "Aj1.....", "arcus")
cursor = db.cursor()

if(os.environ['REQUEST_METHOD'] == "POST"):
	
	username = cgi.FormContent()['username'][0]
	password = cgi.FormContent()['password'][0]
	form = cgi.FieldStorage()
	
	if(form.getvalue('new')):
		query = "INSERT INTO users(username,password) VALUES('{0}','{1}')". format(username,password)
		try:
	   		cursor.execute(query)
		   	db.commit()
		   	
		   	last = cursor.lastrowid
		   	c = Cookie.SimpleCookie()
			c['id'] = last
			print c
			if('HTTP_REFERER' in os.environ):
				print("Location:{0}\r\n\r\n". format(os.environ['HTTP_REFERER']))
			else:
				print("Location:/")
			#print ""
			
		except:
			header.header_content()
		   	print("Username already exist.")
		   	db.rollback()
	
	else:
		query = "SELECT * FROM users WHERE username = '{0}'". format(username)
		try:
		   	cursor.execute(query)
			results = cursor.fetchone()		

			if(results>0 and password == results[2]):
				c = Cookie.SimpleCookie()
				c['id'] = results[0]
				print c
				print("Location:{0}\r\n\r\n". format(os.environ['HTTP_REFERER']))
			else:
				header.header_content()
				print("wrong password")
				
		except:
			header.header_content()
			print "Error: unable to fecth data"


elif(os.environ['REQUEST_METHOD'] == "GET"):

	header.header_content()
	#print(os.environ)
	print """

    <div class="login-dark">
        <form action="/login.py" method="POST">
            <h2>Login Form</h2>
            <div class="illustration"><i class="icon ion-ios-locked-outline"></i></div>
            <div class="form-group">
                <input class="form-control" type="text" name="username" placeholder="USERNAME">
            </div>
            <div class="form-group">
                <input class="form-control" type="password" name="password" placeholder="PASSWORD">
            </div>
            <div class="checkbox">
                <label>
                    <input type="checkbox" name="new">SIGN-UP</label>
            </div>
            <div class="form-group">
                <button class="btn btn-primary btn-block" type="submit">LOG-IN </button>
            </div>
        </form>
    </div>
    <script src="/js/jquery.min.js"></script>
    <script src="/bootstrap/js/bootstrap.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.15/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.15/js/dataTables.bootstrap.min.js"></script>
    <script src="/js/script.min.js"></script>
</body>

</html>

	"""

