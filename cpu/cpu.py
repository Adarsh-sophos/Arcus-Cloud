#!/usr/bin/python2


import cgi
import commands

print "content-type: text/html"
print

print commands.getoutput("grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage "%"}'")
