#coding = utf-8
import requests
import time
import Tkinter
Ver = 0
url = "https://raw.githubusercontent.com/NKUCodingCat/RSS-for-NKU/master/RSS-for-NKU-SMS/"
xml_set=[
		'kydt.xml',
		'xwzx.xml',
		'bksjx.xml',
		'yjsjx.xml',
		'xsgz.xml',
		'zsxx.xml'
	]
def update ():
	for i in xml_set:
		requests.get(url+i)
if __name__ == '__main__':
	update()
	while 1:
		time.sleep(0.5)
		if not int(time.time())%60:
			VerNow = int(requests.get(url+"Version").content)
			if VerNow > Ver:
				update()
				Ver = VerNow
				print "updated"
			else:
				pass