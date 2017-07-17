#!/usr/bin/python2


import cgi
import commands
import cgitb
cgitb.enable()

print commands.getoutput('date').split(' ')[4]
