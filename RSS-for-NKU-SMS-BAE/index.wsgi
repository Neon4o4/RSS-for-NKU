# -*- coding: utf-8 -*-
import sae
import up
import time
import re
a  = re.compile("\.xml")
import os
import mail
from sae.ext.storage import monkey

monkey.patch_all()

CheckTime = 1800

import sae.storage
def storage(name):
    s = sae.storage.Client()
    ob = s.get('test',name)
    data = ob.data
    url = s.url('test',name)
    return url
def app(environ, start_response):
    f = open ("/s/test/Version","r")
    try:
    	g = open ("/s/test/Now","r")
    except:
        g = open ("/s/test/Now","w")
        g.write("0")
        g.close()
        g = open ("/s/test/Now","r")
    Ver = re.sub("[^\d]","",g.read())
    N = "<html><head></head><body><h3>\n	This is the News from NKU, developed by CodingCat/Neon4o4\n</h3>\n<p>\n\t<br>\n</p>\n<pre>The news version(marked by timestamp) is :\t"+f.read()+"\nThe whole world are  at  : \t\t\t"+str(int(time.time()))+"\nAnd the next check will be at : \t\t"+str(int(Ver)+CheckTime)+"\n</pre>\n<p>\n	<br>\n</p>\n<h4>\n	SMS-News lists:\n</h4>\n"
    M = os.listdir("/s/test/")
    status = '200 OK'
    response_headers = [('Content-type', 'text/html')]
    start_response(status, response_headers)
    f.close()
    for i in M:
        if a.findall(i):
            N+="\n"          
            N += "<pre>"+i+"<a href=\""+storage(i)+"\">"+storage(i)+"</a>&nbsp;</pre>\n"
    N += "<p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p style=\"text-align:center;\">\nBlog of us : <a href=\"https://github.com/NKUCodingCat\" target=\"_blank\">CodingCat</a>/<a href=\"https://github.com/Neon4o4\" target=\"_blank\">Neon4o4</a>\n</p>\n<p style=\"text-align:center;\">\nProject website:<a href=\"https://github.com/NKUCodingCat/RSS-for-NKU/tree/master/RSS-for-NKU-SMS-BAE\" target=\"_blank\">Here</a><span id=\"__kindeditor_bookmark_end_216__\"></span>\n</p>"
    N += "</body>\n</html>\n"
    if time.time()-(int(Ver))>CheckTime:
        up.up()
        return["<html><head></head><body><pre>Updating...........please refresh several seconds later\n\t\t\t\t\t-----CodingCat</pre></body></html>"]
    return [str(N)]

application = sae.create_wsgi_app(app)