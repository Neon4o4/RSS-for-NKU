import httplib
import re
import Catch
from sgmllib import SGMLParser
from sae.mail import EmailMessage
ToList = ["446709220@qq.com"]

HTML = "<html><head></head><body><meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\"><h2 style=\"text-align:center;\">"
#--------Title--------------
HTML1 = "</h2><h4 style=\"text-align:center;\">"
#--------Time---------------
HTML2 = "</h4><p><a href=\""
#--------Link---------------
HTML3 = "\" target=\"_blank\">Click Here to The Source Page</a></p><p>"
#--------Text---------------
HTML4 = "</p><p><br></p></body></html>"


def get_time_and_text(url):
    Save = "/s/test/SRC"
    conn=httplib.HTTPConnection('sms.nankai.edu.cn')
    conn.request('GET', url)
    httpres = conn.getresponse() 
    TE = httpres.read()
    f = open(Save,"w")
    f.write(TE)
    f.close()
    time = re.findall('\d+-\d+-\d+',TE)[0]
    text = Catch.Catch(Save)
    conn.close()
    
    return (time,text)

def Create_Text(title,link):
    T_T = get_time_and_text(link)
    ANS = HTML + title + HTML1 + T_T[0] + HTML2 +"http://sms.nankai.edu.cn/"+ link + HTML3 + T_T[1] +HTML4
    return re.sub("class=\"[^<>]+\"","style=\"text-align:center;\"",ANS)




def send_mail(Title,Text):
	m = EmailMessage()
	m.to = ToList
	m.subject = Title
	m.html = Text
	m.smtp = ('smtp.yeah.net',25, 'nkusmsrss@yeah.net', 'pWS', False)
	m.send()
    
    
def Create_HTML_UP(sth_new):
    if len(sth_new) == 0:
        return None
    else:
        for i in sth_new:
            Title = i[1]
            Text = Create_Text(i[1],i[0])
            send_mail(Title,Text)

