from sae.mail import EmailMessage

import time
import NUM
import re
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



def AvaClr():
    L = list(set(GetAva()))
    print L
    PutAva(L)
    
    
def TmpClr():
    T = time.time()
    D = GetTmp()
    for i in D.keys():
        if  T - D[i]["time"] > 86400:
            del D[i]
    PutTmp(D)



def send_mail(Email,Title,Text):
	m = EmailMessage()
	m.to = Email
	m.subject = Title
	m.html = Text
	m.smtp = ('smtp.126.com',25, 'nkumailvali@126.com', 'PSW', False)
	m.send()


def Temp_in(Email, Code, Time, Todo):
    
    
    
    D = {}
    D["vcode"] = str(Code)
    D["time"] = Time
    D["todo"] = Todo
    Dict = GetTmp()
    try:
        Key = Dict[Email]
        if time.time() - Dict[Email]["time"] < 60:
            Dict[Email]["time"] = time.time()
            PutTmp(Dict)
            return "Please wait 60 Seconds"
        else:
            send_mail(re.sub("%40","@",Email),"ValidateMail","Please go to http://2.nkursstest.sinaapp.com/ and input the Validate Code :"+str(Code)+" and your Email Address,Click validate,the Code can be used in 24 H ")
            Dict[Email] = D
            PutTmp(Dict)
            TmpClr()
            return "Mail Sent"
    except:
        send_mail(re.sub("%40","@",Email),"ValidateMail","Please go to http://2.nkursstest.sinaapp.com/ and input the Validate Code :"+str(Code)+" and your Email Address,Click validate,the Code can be used in 24 H ")
        Dict[Email] = D
        PutTmp(Dict)
        return "Mail Sent"


def CheckMail(Email,Code):
    Dict = GetTmp()
    try:
        Key = Dict[Email]
    except:
        return False
    
    if time.time() - Dict[Email]["time"] > 86400:
        del Dict[Email]
        PutTmp[Dict]
        return False
    
    
    
    elif Dict[Email]["vcode"] != Code:
        return False
    
    
    
    else:
        if Dict[Email]["todo"] == "in":
            List = GetAva()
            List.append(Email)
            PutAva(List)
            del Dict[Email]
            PutTmp(Dict)
        else:
            List = GetAva()
            LL = []
            for i in List:
                if i != Email:
                    LL.append(Email)
            PutAva(LL)
            del Dict[Email]
            PutTmp[Dict]
        AvaClr()
        return True
    
