from sae.mail import EmailMessage

import time


import sae.kvdb
kv = sae.kvdb.KVClient()





def GetAva ():
    return kv.get("Ava")

def PutAva (List):
    return kv.set("Ava",List)

def GetTmp ():
    return kv.get("Tmp")

def PutTmp (Dict):
    return kv.set("Tmp",Dict)





def send_mail(Email,Title,Text):
	m = EmailMessage()
	m.to = Email
	m.subject = Title
	m.html = Text
	m.smtp = ('smtp.yeah.net',25, 'nkusmsrss@yeah.net', 'PSW', False)
	m.send()


def Temp_in(Email, Code, Time):
    
    aend_mail(Email,"ValidateMail","Please go to http://2.nkursstest.sinaapp.com/ and input the Validate Code :"+str(Code)+" and your Email Address,Click validate,the Code can be used in 24 H ")
    
    D = {}
    D["vcode"] = str(Code)
    D["time"] = Time
    Dict = GetTmp()
    Dict[Email] = D
    PutTmp(Dict)
    return True


def CheckMail(Email,Code):
    Dict = GetTmp()
    try:
        Key = Dict[Email]
    except:
        return False
    if Dict[Email]["vcode"] != Code:
        return False
    elif time.time() - Dict[Email]["time"] > 86400:
        return False
    else:
        return True
    
