# -*- coding: utf-8 -*-
import sae
import up
import time
import re
import datetime
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
    T = f.read()
    try:
    	g = open ("/s/test/Now","r")
    except:
        g = open ("/s/test/Now","w")
        g.write("0")
        g.close()
        g = open ("/s/test/Now","r")
    Ver = re.sub("[^\d]","",g.read())
    Time = int(Ver)
    if (time.time() - Time)>CheckTime:
        sth_new = up.up()
        status = '200 OK'
        response_headers = [('Content-type', 'text/html')]
        start_response(status, response_headers)
        mail.Create_HTML_UP(sth_new)
        return["<html><head><meta http-equiv=\"refresh\" content=\"2\"></head><body><pre>Updating...........please wait several seconds\n\t\t\t\t\t-----CodingCat</pre></body></html>"]
    else:
        
        N = "<html><head><link href=\"http://nkursstest-test.stor.sinaapp.com/a.css\" rel=\"stylesheet\" type=\"text/css\" /></head><body><h3>\n	This is the News from NKU, developed by CodingCat/Neon4o4\n</h3><pre>The news version(marked by timestamp) is :\t"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(T)))+"</pre><pre>The whole world are  at  : \t\t\t"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))+"</pre><pre>And the next check will be at : \t\t"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(Ver)+CheckTime))+"\n</pre>\n<p>\n	<br>\n</p>\n<h4>\n	SMS-News lists:\n</h4>\n"
        M = os.listdir("/s/test/")
  
    
        f.close()
        for i in M:
            if a.findall(i):
                N+="\n"          
                N += "<pre>"+i+"\t<a href=\""+storage(i)+"\">"+storage(i)+"</a>&nbsp;</pre>\n"
        N += "<p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p><br /></p><p style=\"text-align:center;text-indent:0em;\">Mail Alert Service is avaliable. If you want to recevice the mail please <a href=\"Mailto:nankai.codingcat@outlook.com\">tell me</a></p><p style=\"text-align:center;text-indent:0em;\">Blog of us : <a href=\"https://github.com/NKUCodingCat\" target=\"_blank\">CodingCat</a>/<a href=\"https://github.com/Neon4o4\" target=\"_blank\">Neon4o4</a>\n</p>\n<p style=\"text-align:center;text-indent:0em;\">\nProject Home:<a href=\"https://github.com/NKUCodingCat/RSS-for-NKU/tree/master/RSS-for-NKU-SMS-BAE\" target=\"_blank\">Here</a><span id=\"__kindeditor_bookmark_end_216__\"></span>\n</p><p>TimeStamp for Further Dev :"+T+"</p>"
        N += "</body>\n</html>\n"
    
        status = '200 OK'
        response_headers = [('Content-type', 'text/html')]
        start_response(status, response_headers)
        return [str(N)]

application = sae.create_wsgi_app(app)