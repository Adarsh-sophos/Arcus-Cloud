#!/usr/bin/python2

import cgi,commands

import header

header.header_content()

print """
    
    <div class="features-boxed">
        <div class="alert alert-info text-center hidden" role="alert">
            <button type="button" class="close" data-dismiss="alert" aria-label="Close"> <span aria-hidden="true">x</span></button> <span style="margin:auto;"> <strong>Alert</strong> text.</span> </div>
        <div class="container">
            <div class="intro">
                <h2 class="text-center" style="font-size:74px;font-family:Oswald, sans-serif;color:rgb(23,59,95);">ARCUS </h2>
                <p class="text-center" style="font-family:Roboto, sans-serif;">A low-level cloud for your high level solutions!!</p>
            </div>
        </div>
    </div>
    <div class="projects-clean">
        <div class="container">
            <div class="intro"></div>
            <div class="row projects">
                <div class="col-lg-4 col-sm-6 item" data-bs-hover-animate="pulse"><img class="img-responsive" src="/img/svg_cloud_nfs.jpg">
                    <p class="description" style="font-size:21px;">Object </p>
                </div>
                <div class="col-lg-4 col-sm-6 item" data-bs-hover-animate="pulse"><img class="img-responsive" src="/img/cloud-web-small.jpg">
                    <p class="description">CAAS </p>
                </div>
                <div class="col-lg-4 col-sm-6 item" data-bs-hover-animate="pulse"><img class="img-responsive" src="/img/saas.jpg">
                    <p class="description" style="font-size:21px;">PAAS </p>
                </div>
                <div class="col-lg-4 col-sm-6 item"><img class="img-responsive" src="/img/svg_cloud_nfs.jpg">
                    <p class="description">IAAS</p>
                </div>
                <div class="col-lg-4 col-sm-6 item" data-bs-hover-animate="pulse"><img class="img-responsive" src="/img/server.png">
                    <p class="description">DBaaS</p>
                </div>
                <div class="col-lg-4 col-sm-6 item" data-bs-hover-animate="pulse"><img class="img-responsive" src="/img/arcus-control-c.jpg">
                    <p class="description" style="font-size:21px;">DEPLOY | MANAGE | BALANCE CONTAINER</p>
                </div>
            </div>
        </div>
    </div>
    <script src="/js/jquery.min.js"></script>
    <script src="/bootstrap/js/bootstrap.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.15/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/1.10.15/js/dataTables.bootstrap.min.js"></script>
    <script src="/js/script.min.js"></script>
"""

#require.require("footer.py")
