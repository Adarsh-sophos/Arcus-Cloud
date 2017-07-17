#!/usr/bin/python2

import config
import header
import cgi,commands,os,MySQLdb

header.header_content()

if(os.environ['REQUEST_METHOD'] == "GET"):
	
	db = MySQLdb.connect("localhost","root", "Aj1.....", "arcus")
	cursor = db.cursor()
	
	user_id = header.cookie_value()
	
	print """
		<div class="panel panel-primary">
		<div class="panel-heading">NFS Storage History</div>
		<div class="panel-body"> """
	
	print """
<table class="table table-striped table-hover">
	<thead>
		<tr>
			<th style="text-align:center;">Number</th>
			<th style="text-align:center;">Drive Size</th>
			<th style="text-align:center;">Extend</th>
			<th style="text-align:center;">Remove</th>
			<th style="text-align:center;">Unmount/Mount</th>
			<th style="text-align:center;">Snapshot</th>
		<tr>
	</thead>

	<tbody> """
	
	sql = "SELECT * FROM nfs WHERE user_id={0}". format(user_id)
	try:
	   	cursor.execute(sql)
		results = cursor.fetchall()
	except:
		print "Error: unable to fecth data"
	
	i=1
	for row in results:
		print("<tr>")
		print('<td style="text-align:center;">' + str(i) + "</td>")
		print('<td style="text-align:center;">' + str(row[2]) + "</td>")
		print('<td style="text-align:center;"> <form action="/activity_execute.py?service=extend&id={1}&type=nfs" method="POST"><input type="text" name="extendSize" placeholder="current:{0} MB"/> <button type="submit">Extend</button></form> </td>'. format(row[2], row[0]))
		print('<td style="text-align:center;"> <form action="/activity_execute.py?service=remove&id={0}&type=nfs" method="POST"> <button type="submit">Remove</button></form></td>"'. format(row[0]))
		
		if(row[6] == 'm'):
			print('<td style="text-align:center;"> <form action="/activity_execute.py?service=unmount&id={0}&type=nfs" method="POST"> <button type="submit">Unmount</button></form></td>"'. format(row[0]))
		else:
			print('<td style="text-align:center;"> <form action="/activity_execute.py?service=mount&id={0}&type=nfs" method="POST"> <button type="submit">Mount</button></form></td>"'. format(row[0]))
		print('<td style="text-align:center;"> <form action="/activity_execute.py?service=snapshot&id={0}&type=nfs" method="POST"> <button type="submit">Snap</button></form></td>"'. format(row[0]))
		print("</tr>")
		
		n = "SELECT * FROM snapshot WHERE nfs_id={0}". format(row[0])
		try:
		   	rs = cursor.execute(n)
		   	if(rs != 0):
				a = cursor.fetchall()
				
				j=1
				for b in a:
					print("<tr>")
					print('<td></td>')
					print('<td></td>')
					print('<td></td>')
					print('<td></td>')
					print('<td></td>')
					print('<td style="text-align:center;"><a href="/recover.py?n={0}&id={3}">snap-{1} {2}</a></td>'. format(b[2], j, b[3], b[1]))
					print("</tr>")
					j+=1
			
		except:
			print "Error: unable to fecth data"
		
		i+=1
	
	print("</tbody>")
	print("</table>")
	print("</div></div></div>")
	
	
	# iscsi server
	print """
		<div class="panel panel-primary">
		<div class="panel-heading">iSCSI Storage History</div>
		<div class="panel-body"> """
		
	print """
<table class="table table-striped table-hover">
	<thead>
		<tr>
			<th style="text-align:center;">Number</th>
			<th style="text-align:center;">Drive Size</th>
			<th style="text-align:center;">Extend</th>
			<th style="text-align:center;">Login/Logout</th>
			<th style="text-align:center;">Snapshot</th>
		<tr>
	</thead>

	<tbody> """
	
	sql = "SELECT * FROM iscsi WHERE user_id={0}". format(user_id)
	try:
	   	cursor.execute(sql)
		results = cursor.fetchall()
	except:
		print "Error: unable to fecth data"
		
	i=1
	for row in results:		
		
		print("<tr>")
		print('<td style="text-align:center;">' + str(i) + "</td>")
		print('<td style="text-align:center;">' + str(row[2]) + "</td>")
		print('<td style="text-align:center;"> <form action="/activity_execute.py?service=extend&id={1}&type=iscsi" method="POST"><input type="text" name="extendSize" placeholder="current:{0} MB"/> <button type="submit">Extend</button></form> </td>'. format(row[2], row[0]))
		
		if(row[4] == 'login'):
			print('<td style="text-align:center;"> <form action="/activity_execute.py?service=logout&id={0}&type=iscsi" method="POST"> <button type="submit">Logout</button></form></td>"'. format(row[0]))
		else:
			print('<td style="text-align:center;"> <form action="/activity_execute.py?service=login&id={0}&type=iscsi" method="POST"> <button type="submit">Login</button></form></td>"'. format(row[0]))
		print('<td style="text-align:center;"> <form action="/activity_execute.py?service=snapshot&id={0}&type=iscsi" method="POST"> <button type="submit">Snap</button></form></td>"'. format(row[0]))
		print("</tr>")
		
		n = "SELECT * FROM snapshot_iscsi WHERE iscsi_id={0}". format(row[0])
		try:
		   	rs = cursor.execute(n)
		   	if(rs != 0):
				a = cursor.fetchall()
				
				j=1
				for b in a:
					print("<tr>")
					print('<td></td>')
					print('<td></td>')
					print('<td></td>')
					print('<td></td>')
					print('<td style="text-align:center;"><a href="/recover.py?n={0}">snap-{1} {2}</a></td>'. format(b[2], j, b[3]))
					print("</tr>")
					j+=1
			
		except:
			print "Error: unable to fecth data"
		
		i+=1
                                

	print("</tbody>")
	print("</table>")
	print("</div></div></div>")

print """
    <script src="/js/jquery.min.js"></script>
    <script src="/bootstrap/js/bootstrap.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.15/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.15/js/dataTables.bootstrap.min.js"></script>
    <script src="/js/script.min.js"></script>
</body>

</html>
"""
	
	
	
