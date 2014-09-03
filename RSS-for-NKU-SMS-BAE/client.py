#coding = utf-8
import requests
import time,sys
if sys.version < '3':
    from Tkinter import *
else:
    from tkinter import *
def showMessage():
    # show reminder message window
    root=Tk()
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry("+%d+%d" % (x, y))
    root.protocol('WM_TAKE_FOCUS', root.update )
    root.wait_visibility(root)
    root.attributes('-topmost',1)
    label=Label(root, text="Do what you should do.").pack({"side": "left"})
    button=Button(text="OK", width="10", command=lambda:root.destroy()).pack()
    root.mainloop()

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
		if not int(time.time())%10:
			VerNow = int(requests.get(url+"Version").content)
			if VerNow > Ver:
				update()
				Ver = VerNow
				showMessage()


			else:
				pass