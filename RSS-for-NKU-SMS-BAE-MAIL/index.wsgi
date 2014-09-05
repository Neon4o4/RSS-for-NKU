#-*- coding=utf-8 -*-



GETDATA = """<html><head><title>E-mail Validate</title></head>
<body>
<h3>NKU-RSS-SAE-TEST Proj Mail Alert Service Manage Page</h3>
<p>Input your Email Address and Click subscribe or unsubscribe, you will receive an Validate Email and do What Email want you to do </p>
<p>If you want Click subscribe or unsubscribe ,there is no need to input Validate Code, Because We will ignore it :-)</p>
<form action=\"\"name=\"form1\"method=\"post\">
Your Email<input type=\"text\"name=\"Email\"/><br/>
Validate Code<input name=\"Code\"></textarea><br/>
<input type=\"submit\"name=\"In\"value=\"Validate\"/>
<input type=\"submit\"name=\"In\"value=\"Subscribe\"/>
<input type=\"submit\"name=\"In\"value=\"Unsubscribe\"/>
</form>
<a href = "http://nkursstest.sinaapp.com">RSS Home</a></body></html>
"""

import re

import sae

import urlparse

import xml.etree.ElementTree as ET

from sae.ext.storage import monkey


import kvpo


Ma = re.compile(u"\S+%40\S+\.\S+")
N = re.compile("[^\d]")


def app(environ, start_response):

    status = '200 OK'

    response_headers = [('Content-type', 'text/html; charset=utf-8')]

    start_response(status, response_headers)

    method=environ['REQUEST_METHOD']

    if method=="GET":

        return GETDATA

    elif method=="POST":
        
        Dict = {}

        post=environ['wsgi.input']
        
        post = post.read()
        
        List = re.split("&",post)
        
        for i in List:
            
            M =  re.split("=", i)
            
            try:
            
            	Dict [M[0]] = M[1]
                
            except:
                
                pass
            
            
        if not Ma.findall(Dict["Email"] ):
            
            return "Mail Addr ERR"
        #++++++++++++++++++++++++++++++++++++++
        if Dict["In"] == "Validate":
        
            if N.findall(Dict["Code"]):
            
                return "Validate Code ERR"
        
        
            if kvpo.CheckMail(Dict["Email"],Dict["Code"]):
            
                return "Mail Validate Success~~~~"
       
            else:
            
                return "Validate Failed, TimeOut or Validate Code Error or No such Email Address Record"
        #==========================================
        if Dict["In"] == "Subscribe":
            return "DEVing"
        if Dict["In"] == "Unsubscribe":
            return "DEVing"
        
application = sae.create_wsgi_app(app)

