Dict = {"01":"Jan","02":"Feb","03":"Mar","04":"Apr","05":"May","06":"Jun","07":"Jul","08":"Aug","09":"Sep","10":"Oct","11":"Nov","12":"Dec"}
Da = [""]+["st","nd","rd"]+ ["th"]*17 + ["st","nd","rd"]+ ["th"]*7 + ["st","nd","rd"]
We = ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
def Zeller(y,m,d):
	c = int(y[0:2])
	y = int(y[2:])
	m = int(m)
	d = int(d)
	if m < 3:
		m += 12
		y -= 1
	w=y+y/4+c/4-2*c+((26*(m+1))/10)+d-1
	return We[w%7]
def DateTran(DATE):
	M = Dict[DATE[5:7]]
	if DATE[-2] == "0":
		D = DATE[-1]
	else:
		D = DATE[-2:]
	return Zeller(DATE[0:4],DATE[5:7],D) +" "+ D +Da[int(D)]+ " " + M + " " +  DATE[0:4]