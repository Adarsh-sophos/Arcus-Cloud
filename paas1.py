#!/usr/bin/python2

import config
import header
import cgi,commands,os,MySQLdb
#import cgitb; cgitb.enable()

header.header_content()

if(os.environ['REQUEST_METHOD'] == "POST"):
	form = cgi.FieldStorage()
	
	print(form)
	# Get filename here.
	fileitem = form['filename']
	#os = form['os']

	# Test if the file was uploaded
	if fileitem.filename:
		# directory traversal attacks
		fn = os.path.basename(fileitem.filename)
		open('/Arcus/public/tmp/' + fn, 'wb').write(fileitem.file.read())

		# start docker container
		commands.getstatusoutput("sudo docker run -dit --name {0} apacheimage:v1". format(header.cookie_value()))
		commands.getstatusoutput("sudo docker cp '/Arcus/public/tmp/{0}' {1}:/var/www/html/". format(fn, header.cookie_value()))
		ip = commands.getstatusoutput('sudo docker inspect {0} | jq ".[].NetworkSettings.Networks.bridge.IPAddress"'. format(header.cookie_value()))
		print(ip[1])

	else:
	   	message = 'No file was uploaded'
	


elif(os.environ['REQUEST_METHOD'] == "GET"):
	
	print """
<div class="form-photo">
      <div class="form-container">
			<div class="panel panel-primary">
			  <div class="panel-heading">Launch a container</div>
			  <div class="panel-body">
			  		<form method="POST" action="/paas1.py" enctype="multipart/form-data">
                		<h2 class="text-center">Website</h2>                		
                		
			  			<select name="os">
							<option value="1">CentOS</option>
							<option value="2">Ubuntu</option>
							<option value="3">Fedora</option>
						</select>						  
					  	
					  	<p>File: <input type="file" name="filename" /></p>
					  	
					  	<div class="form-group">
				            <button class="btn btn-primary btn-block" type="submit">SUBMIT </button>
				        </div>	
			  			
			  		</form>
			  </div>
			</div>
	</div>
</div>


<div class="panel panel-primary">
			  <div class="panel-heading">Online Compiler</div>
			  <div class="panel-body">
			  	<form action="/paas.py" id="form" method="POST">
			  		<select class="select" id="language">
						<option value="1">C</option>
						<option value="2">php</option>
						<option value="3">python 2.7</option>
						<option value="4">python 3</option>
					</select>
					
			  		<div class="form-group">
						<textarea class ="form-control" id="code" rows="10" cols="50"></textarea>
					</div>
					
					<div class="form-group">
						Input:
						<textarea class ="form-control" id="input"></textarea>
					</div>
			  		
			  		<button type="submit">Run</button>
	
				</form>
		  
			  <iframe id='output'></iframe>
		</div>
	</div>

<script src="/js/jquery.min.js"></script>
	
	<script>
	$("#form").submit( function(){
    	
    	var code = $('textarea#code').val();
    	var input = $('textarea#input').val();
    	var language = $('#language').val();

        $.ajax({
		  type: 'POST',
		  url: '/code_execute.py',
		  data: { 'code' : code, 'language': language, 'input': input },
		  dataType: 'json',
		  success: function(d) {
			$('#output').contents().find('html').html("<pre> "+ d.output + " </pre>");
		  },
		  error: function() {
			$('#output').contents().find('html').html("<h4>Empty File</h4>")
		  }
		}); 
    
    return false;
    });
	</script>
	"""

print """
    <script src="/bootstrap/js/bootstrap.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.15/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.15/js/dataTables.bootstrap.min.js"></script>
    <script src="/js/script.min.js"></script>
</body>

</html>
"""









