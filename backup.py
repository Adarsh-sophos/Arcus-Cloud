#!/usr/bin/python2

import time,commands,datetime
import sys

toolbar_width = 60

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

def progress():
	for i in range(2):
		# update the bar
		sys.stdout.write("#"*30)
		time.sleep(0.5)
		sys.stdout.flush()

	sys.stdout.write("\n")

commands.getstatusoutput("sudo mkdir /backup")

sys.stdout.write("Copying access logs...\n")
commands.getstatusoutput("sudo cp /var/log/httpd/access_log /backup")
progress()

sys.stdout.write("Copying error logs...\n")
commands.getstatusoutput("sudo cp /var/log/httpd/error_log /backup")
progress()

sys.stdout.write("Copying conf files...\n")
commands.getstatusoutput("sudo cp /etc/httpd/conf.d/cgi.conf /backup")
progress()

sys.stdout.write("Dumping database...\n")
progress()

sys.stdout.write("Compressing...\n")

time = datetime.datetime.now().strftime('%d-%h-%Y-%H-%M-%S')
commands.getstatusoutput("zip -r /backup/{0}.zip /backup". format(time))

commands.getstatusoutput("sshpass -p redhat scp /backup/{0}.zip root@192.168.43.249:/root/Documents". format(time))
commands.getstatusoutput("sshpass -p redhat scp /backup/{0}.zip root@192.168.43.111:/storage/emulated/backups". format(time))















