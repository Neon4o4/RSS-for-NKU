# -*- coding: utf-8 -*-
import sae
import up
import time
import re
a  = re.compile("\.xml")
import os
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
    N = "This is the News from NKU SMS, developed by CodingCat/Neon4o4\nThe news version is : \t\t"+f.read()+"\nNow is :\t\t\t"+str(int(time.time()))+"\nAnd the next check will be at : "+str(int(Ver)+CheckTime)+"\n\nNeews lists:\n"
    M = os.listdir("/s/test/")
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    f.close()
    for i in M:
        if a.findall(i):
            N+="\n"
            
            N+=i
            N+="\t"
            N+=storage(i)
    if time.time()-(int(Ver))>CheckTime:
        up.up()
        return["Updating...........please refresh several seconds later\n\t\t\t\t\t-----CodingCat"]
    return [str(N)]

application = sae.create_wsgi_app(app)