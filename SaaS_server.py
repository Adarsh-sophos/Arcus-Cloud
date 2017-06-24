'''
1. create a user(see 3(b))
2. enable X11 forwarding --> /etc/ssh/sshd_config --> linenumber 115 --> X11Forwarding yes
3. Restricting user -
		(a) Restrict user to access a particular program (NOT WORKING)
			>> setfacl -m u:username:- /usr/bin/gnome-terminal[program path]
			
		(b) create an application specific user
			>> useradd -s /usr/bin/firefox username
			
			to unblock some services -
			>> setfacl -m u:username:rx /usr/bin/gnome-terminal[program path]
'''


