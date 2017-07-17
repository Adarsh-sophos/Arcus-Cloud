#!/usr/bin/python2

import header
import commands,cgi
import cgitb
cgitb.enable(display=0, logdir="log/log.txt")

header.header_content()

dockerV = commands.getoutput("docker -v")
runningCount = commands.getoutput("sudo docker info | grep Running:").split(" ")[2]
pausedCount = commands.getoutput("sudo docker info | grep Paused:").split(" ")[2]
exitedCount = commands.getoutput("sudo docker info | grep Stopped:").split(" ")[2]

print ('<div class="main-holder">')
print ('<div class="form-container" style="margin-left:150px auto;margin-right:150px auto;">')
#modal
print ('<!-- Modal -->')
print ('<div class="modal fade" id="myModal" role="dialog">')
print ('<div class="modal-dialog">')
print ('')
print ('<!-- Modal content-->')
print ('<div class="modal-content">')
print ('<div class="modal-header" style="padding:35px 50px;">')
print ('<button type="button" class="close" data-dismiss="modal">&times;</button>')
print ('<h4><span class="text-center "></span> Login</h4>')
print ('</div>')
print ('<div class="modal-body" style="padding:40px 50px;">')
print ('<form role="form">')
print ('<div class="form-group">')

print ('<label for="IP"><span class="text-center"></span> IP Address:</label>')
print ('<div id="modIP"> </div>')

print ('</div>')
print ('<div class="form-group">')
print ('<iframe href="#" width="100%"></iframe>')
print ('</div>')
print ('</form>')
print ('</div>')
print ('<div class="modal-footer">')
print ('<button type="submit" class="btn btn-danger btn-default pull-right" data-dismiss="modal"><span class="text-center"></span> Cancel</button>')
print ('</div>')
print ('</div>')

print ('</div>')
print ('</div> ')


print ('<form style="width:700px;">')
print ('<h2 class="text-center">CONTAINER PANEL</h2>')
print ('<div class="table-responsive">')
print ('<table class="table table-bordered table-hover">')
print ('<thead class="thead-default">')
print ('<tr>')
print ('<th colspan="3" style="text-decoration:underline;border-radius:5px;"> ' + dockerV + ' </th>')
#print ('<th colspan="3" style="border:0;"></th>')
print ("<th colspan='4' style='text-align:center;'><span class='badge' style='background-color:green;'>Running: {} </span>  <span class='badge' style='background-color:orange;'>Paused: {} </span>  <span class='badge' style='background-color:red;'>Stopped: {}</span></th>".format(runningCount,pausedCount,exitedCount))
print ('<th rowspan="1" style="border:0;"></th>')
print ('<th rowspan="1" style="border:0;"></th>')
print ('</tr>')
print ('<tr>')
print ('<th rowspan="1" style="text-align:center;">IMAGE NAME</th>')
print ('<th rowspan="1" style="text-align:center;">CONTAINER NAME</th>')
print ('<th rowspan="1" style="text-align:center;">IP</th>')
print ('<th style="text-align:center;">STATUS</th>')
print ('<th rowspan="2" style="text-align:center;">START</th>')
print ('<th rowspan="2" style="text-align:center;">STOP</th>')
print ('<th rowspan="2" style="text-align:center;">PAUSE</th>')
print ('<th rowspan="2" style="text-align:center;">REMOVE</th>')
print ('<th rowspan="1">SHELL</th>')
print ('<th rowspan="1">INFO</th>')
print ('</tr>')
print ('<tr>')
##print ("<th colspan='1' style='text-align:center;'><span class='badge' style='background-color:green;'>{}</span><span class='badge' style='background-color:orange;'>{}</span><span class='badge' style='background-color:red;'>{}</span></th>".format(runningCount,pausedCount,exitedCount))

print ('</thead>')
print ('<tbody>')
z=1
for i in commands.getoutput("sudo docker ps -a").split('\n'):
	if z==1:
		z+=1
		pass
	else:
		j = i.split()
		cStatus = commands.getoutput("sudo docker inspect {0} | jq '.[]'.State.Status".format(j[-1]))
		cIP = commands.getoutput("sudo docker inspect --format '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' \"$@\" " + j[-1])
		runningCount = cStatus.count("running")
		exitedCount = cStatus.count("exited")
		if cStatus.strip("\"") == "exited":
			sColour = "red";
			tClass = "danger";
			startIsDisabled = ""
			stopIsDisabled = "disabled"
			cPauseState = ""
			cPauseButton = "pause"
			cPauseIsDisabled = "disabled"
		elif cStatus.strip("\"") == "paused":
			sColour = " #FFC300 "
			tClass = "warning";
			startIsDisabled = "disabled"
			cPauseState = "paused"
			cPauseButton = "unpause"
			stopIsDisabled = "disabled"
			cPauseIsDisabled = " "
		elif cStatus.strip("\"") == "running":
			sColour = "green"
			tClass = "active";
			startIsDisabled = "disabled"
			cPauseButton = "pause"
			stopIsDisabled = " "
			cPauseState = ""
			cPauseIsDisabled = ""
		else:
			sColour = "danger"
			cPauseState = "unpause"

		print "<tr class='{0}'><td>".format(tClass) + j[1] + "</td><td>" + j[-1] + "</td><td>" + cIP  + "</td><td style='color:{0};text-align:center;'>".format(sColour) + cStatus.strip("\"") + "</td><td><button value='" + j[-1] + "' onClick='cStart(this.value);' {0}>Start</button></td><td><button value='".format(startIsDisabled) + j[-1] +"' onClick='cStop(this.value);' {0}>Stop</button></td><td><button value='".format(stopIsDisabled) + j[-1] +"' onClick='cPause(this.value,this.innerHTML);' {0}>{1}</button></td><td><button name='cRemove' value='".format(cPauseIsDisabled,cPauseButton) + j[-1] +"' onClick='cRemove(this.value);'>remove</button></td><td><button name='cShell' value='"+ j[-1] +"' onClick='cShell(this.value);'>shell</button></td><td><button type='button' value='"+ j[-1] +"' class='btn btn-info' data-toggle='modal' data-target='#myModal' name='infoBtn'' onClick='doModal(this.value)'>info</button></td></tr>"

		"""
		<tr class='{0}'>
			<td>".format(tClass) + j[1] + "</td>
			<td>" + j[-1] + "</td>
			<td>" + cIP  + "</td>
			<td style='color:{0};text-align:center;'>".format(sColour) + cStatus.strip("\"") + "</td>
			<td>
				<button value='" + j[-1] + "' onClick='cStart(this.value);' {0}>Start</button>
			</td>
			<td>
				<button value='".format(startIsDisabled) + j[-1] +"' onClick='cStop(this.value);' {0}>Stop</button>
			</td>
			<td>
				<button value='".format(stopIsDisabled) + j[-1] +"' onClick='cPause(this.value,this.innerHTML);' {0}>{1}</button>
			</td>
			<td>
				<button name='cRemove' value='".format(cPauseIsDisabled,cPauseButton) + j[-1] +"' onClick='cRemove(this.value);'>remove</button>
			</td>
			<td>
				<button name='cShell' value='"+ j[-1] +"' onClick='cShell(this.value);'>shell</button>
			</td>
			<td>
				<button type='button' value='"+ j[-1] +"' class='btn btn-info' data-toggle='modal' data-target='#myModal' name='infoBtn'' onClick='doModal(this.value)'>info</button>
			</td>
		</tr>"""

print ('</tbody>')
print ('</table>')
print ('</div>')
print ('<div>')
print 
#showBridge = brctl.showall()
#print (brctl.addbr("br0")
print ('<center><button class="btn btn-primary" type="submit" style="background-color:#ff1e3a !important;" onClick="RemStopped();">remove all stopped containers </button>')
print ('<button class="btn btn-primary" type="submit" style="background-color:#ff1e3a !important;" onClick="RemRunning();">remove all running containers </button>')
print ('<button class="btn btn-primary" type="submit" style="background-color:#055ada !important;" onClick="StartStopped();">start all stopped containers </button>')
print ('<button class="btn btn-primary" type="submit" style="background-color:#055ada !important;" onClick="StopRunning();">stop all running containers </button></center>')
print ('</div>')
print ('</form>')
print ('</div>')
print ('</div>')
print ('<script src="js/jquery.min.js"></script>')
print ('<script src="bootstrap/js/bootstrap.min.js"></script>')

print ('<script type="text/javascript">')

print"""

$(document).ready(function(){
    $("#infoModal").click(function(){
        $("#myModal").modal();
        
    });
});

function cStart(cName){
	window.event.returnValue = false;
	document.location="caas-cStart.py?containerName=" + cName;
}
function cStop(cName){
	window.event.returnValue = false;
	document.location="caas-cStop.py?containerName=" + cName;
}
function cPause(cName,cPauseState){
	window.event.returnValue = false;
	document.location="caas-cPause.py?containerName=" + cName + "&cStatus=" + cPauseState;
}
function cRemove(cName){
	window.event.returnValue = false;
	document.location="caas-cRemove.py?containerName=" + cName;
}
function RemStopped(){
	window.event.returnValue = false;
	document.location="caas-RemStopped.py";
}
function RemRunning(){
	window.event.returnValue = false;
	document.location="caas-RemRunning.py";
}
function StartStopped(){
	window.event.returnValue = false;
	document.location='caas-StartStopped.py';
}
function StopRunning(){
	window.event.returnValue = false;
	document.location='caas-StopRunning.py';
}
function cInfo(cName){
cname = cName;
}

</script>
"""

print ('</body>')
print ('</html>')
