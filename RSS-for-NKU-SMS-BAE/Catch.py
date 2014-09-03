import re
S = re.compile("<div id=\"neirong-main\">")
NP = re.compile("<div class=\"tools fc2 tRight\">")
E = re.compile("<div id=\"banquan\">")
def Catch(File):
	f = open (File,"r")
	SRC = f.read()
	str = ""
	pos = 0
	while 1:
		A = ""
		while 1:
			CHR = SRC[pos]
			A+=CHR
			pos += 1
			if CHR == "\n":
				break
		if S.findall(A):
			str += A
			while 1:
				A = ""
				while 1:
					CHR = SRC[pos]
					A+=CHR
					pos += 1
					if CHR == "\n":
						break
				if not E.findall(A):
					if not NP.findall(A):
						str+=A
					else:
						pass
				else:
					f.close()
					return str