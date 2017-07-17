#!/usr/bin/python2

import commands
import json
import cgi

fs = cgi.FieldStorage()

print("Content-type: application/json")
print

result = {}

lang = int(fs.getvalue('language'))
input1 = fs.getvalue('input')

if(lang == 1):
	codeFile = open("/Arcus/public/tmp/prog.c", "w")
	codeFile.write(fs.getvalue('code'))
	codeFile.close()
	status = commands.getstatusoutput("(cd /Arcus/public/tmp/; gcc prog.c)")
	if(status[0] == 0):
		output = commands.getstatusoutput("(cd /Arcus/public/tmp/; echo '{0}' | ./a.out)". format(input1))
	else:
		output = status
	pass

elif(lang == 2):
	codeFile = open("/Arcus/public/tmp/prog.php", "w")
	codeFile.write(fs.getvalue('code'))
	codeFile.close()
	output = commands.getstatusoutput("sudo php /Arcus/public/tmp/prog.php")

elif(lang == 3):
	codeFile = open("/Arcus/public/tmp/prog.py", "w")
	codeFile.write(fs.getvalue('code'))
	codeFile.close()
	output = commands.getstatusoutput("echo '{0}' | sudo python2 /Arcus/public/tmp/prog.py". format(input1))

elif(lang == 4):
	codeFile = open("/Arcus/public/tmp/prog.py", "w")
	codeFile.write(fs.getvalue('code'))
	codeFile.close()
	output = commands.getstatusoutput("echo '{0}' | sudo python3 /Arcus/public/tmp/prog.py". format(input1))
	
result['output'] = output[1]
result['success'] = True

print(json.dumps(result,indent=1))









