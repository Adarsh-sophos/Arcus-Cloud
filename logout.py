#!/usr/bin/python2

import Cookie

# set the cookie to expire
c = Cookie.SimpleCookie()
c['id']=''
c['id']['expires'] = -1

# print the HTTP header
print c
print("Content-type: text/html")
print("Location:/\r\n\r\n")
