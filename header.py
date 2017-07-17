#!/usr/bin/python2

import Cookie,os

def cookie_value():

	if('HTTP_COOKIE' in os.environ):
		cookie_string = os.environ.get('HTTP_COOKIE')
		c = Cookie.SimpleCookie()
		c.load(cookie_string)

		try:
		    data=int(c['id'].value)
		    return data
		    
		except KeyError:
		    return None
	else:
		return None

def header_content(x='a'):
	
	if(x=='r'):
		print("Content-type:text/html")
	
	else:
		print("Content-type:text/html\r\n\r\n")
		
	print """
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Arcus</title>
    <link rel="stylesheet" href="/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Orbitron">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Oswald">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Pacifico">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Quicksand">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto+Slab:300,400|Roboto:300,400,700">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,700">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto+Slab:300,400">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Sacramento">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Seaweed+Script">
    <link rel="stylesheet" href="/fonts/ionicons.min.css">
    <link rel="stylesheet" href="https://cdn.datatables.net/1.10.15/css/dataTables.bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css">
    <link rel="stylesheet" href="/css/styles.min.css">
    <link rel="stylesheet" href="/css/docker.css">
    <link rel="stylesheet" href="/css/styles.css">
    <link rel="stylesheet" href="/fonts/ionicons.min.css">
    
</head>

<body>


<div>
        <nav class="navbar navbar-default navigation-clean-button" style="text-transform:none;">
            <div class="container">
                <div class="navbar-header"><a class="navbar-brand text-uppercase navbar-link" href="/" style="font-family:Oswald, sans-serif;">ARCUS </a>
                    <button class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navcol-1"><span class="sr-only">Toggle navigation</span><span class="icon-bar"></span><span class="icon-bar"></span><span class="icon-bar"></span></button>
                </div>
                <div class="collapse navbar-collapse" id="navcol-1">
                    <ul class="nav navbar-nav">
                        <li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" aria-expanded="false" href="#">StaaS <span class="caret" data-bs-hover-animate="pulse"></span></a>
                            <ul class="dropdown-menu" role="menu">
                                <li role="presentation">Object Storage</li>
                                <li role="presentation"><a href="/nfs.py">NFS</a></li>
                                <li role="presentation"><a href="/sshfs.py">SSHFS</a></li>
                                <li role="presentation"><a href="/iscsi.py">Block Storage</a></li>
                                
                            </ul>
                        </li>
                        <li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" aria-expanded="false" href="#">CaaS <span class="caret"></span></a>
                            <ul class="dropdown-menu" role="menu">
                                <li role="presentation"><a href="/dp.py">Containers Manager</a></li>
                                <li role="presentation"><a href="/docker-launch.py">Container Launcher</a></li>
                               
                            </ul>
                        </li>
                        <li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" aria-expanded="false" href="#">PaaS <span class="caret"></span></a>
                            <ul class="dropdown-menu" role="menu">
                                <li role="presentation"><a href="/paas1.py">Code Here</a></li>
                          
                            </ul>
                        </li>
                        <li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" aria-expanded="false" href="#">IaaS <span class="caret"></span></a>
                            <ul class="dropdown-menu" role="menu">
                                <li role="presentation"><a href="/iaas.py">Use OS</a></li>
                            </ul>
                        </li>
                        <li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" aria-expanded="false" href="#">DBaaS <span class="caret"></span></a>
                            <ul class="dropdown-menu" role="menu">
                                <li role="presentation"><a href="/dbaas.py">Use MySQL Database</a></li>
                            </ul>
                        </li>
                    </ul> """
	if(cookie_value() == None):
		print('<p class="navbar-text navbar-right actions"> <a class="btn btn-default action-button" role="button" href="/login.py">LOGIN </a></p>')
	else:
		print('<p class="navbar-text navbar-right actions"> <a class="btn btn-default action-button" role="button" href="/logout.py">LOGOUT </a></p>')
		print('<p class="navbar-text navbar-right actions"> <a class="btn btn-default action-button" role="button" href="/activity.py">Activity </a></p>')
	
	print """
                </div>
            </div>
        </nav>
    </div>
	"""
