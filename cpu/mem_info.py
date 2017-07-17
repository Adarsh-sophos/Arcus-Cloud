#!/usr/bin/python2


import cgi
import commands

print "content-type: text/html"
print

print commands.getoutput('cat /proc/meminfo').split('\n')[2]