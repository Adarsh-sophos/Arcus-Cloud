#!/usr/bin/python2

import config
import header
import cgi,commands,os,MySQLdb

header.header_content()

print """

<form action="/paas.py" id="form" method="POST">

	<div>
	  	<label for="language">Select language:</label>
		  <select class="select" id="language">
			<option value="1">C</option>
			<option value="2">php</option>
			<option value="3">python 2.7</option>
			<option value="4">python 3</option>
		  </select>
	</div>

	<div class="form-group">
		<textarea class ="form-control" id="code" rows="10" cols="50" style="width:auto;display: block;margin-left: auto;margin-right: auto;"></textarea>
	</div>
	<div class="form-group">
		Input:
		<textarea class ="form-control" id="input" rows="5" cols="50" style="width:auto;display: block;margin-left: auto;margin-right: auto;"></textarea>
	</div>
	<button type="submit">Run</button>
	
</form>
	
	<iframe id='output'></iframe>

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
