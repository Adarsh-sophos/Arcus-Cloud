#!/usr/bin/python2

import cgi,commands

import header

if(os.environ['REQUEST_METHOD'] == "POST"):
		psss

elif(os.environ['REQUEST_METHOD'] == "GET"):

	print """

    <div class="login-clean">
        <form method="post">
            <h2 class="sr-only">Login Form</h2>
            <div class="illustration"><img src="/img/arcus_logo.png" width="100%" height="100%"></div>
            <div class="form-group">
                <div class="table-responsive">
                    <table class="table">
                        <thead>
                            <tr>
                                <th>
                                    <div class="radio">
                                        <label class="control-label">
                                            <input type="radio" name="serverCount" checked="">Single</label>
                                    </div>
                                </th>
                                <th>
                                    <div class="radio">
                                        <label class="control-label">
                                            <input type="radio" name="serverCount">Multiple</label>
                                    </div>
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr></tr>
                        </tbody>
                    </table>
                </div>
                <input class="form-control" type="text" name="serverIP" placeholder="Remote server IP">
            </div>
            <div class="form-group">
                <input class="form-control" type="password" name="serverPassword" placeholder="Remote server root password">
            </div>
            <div class="form-group">
                <button class="btn btn-primary btn-block" type="submit">Continue </button>
            </div>
        </form>
    </div>
    <script src="/js/jquery.min.js"></script>
    <script src="/bootstrap/js/bootstrap.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.15/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.15/js/dataTables.bootstrap.min.js"></script>
    <script src="/js/script.min.js"></script>
</body>

</html>
	"""
