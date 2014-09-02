#encoding=utf8
#==========================================================
#getPages():  �������ӻ�ȡ��ҳ����
#getURLs():  ����ҳ�����л�ȡ���ŵ�����
#getTitles():  ����ҳ�����л�ȡ���ŵı���
#check_updated():  ���ĳ�����ŷ����Ƿ��и���
#do_update():  ����ĳ�����ŷ����XML�ļ�
#creat_item():  �����������Ӻͱ��ⴴ��XML��ʽ���������ݽڵ�
#getNewItems():  �����и��µ����ݴ���XML��ʽ�����Žڵ�
#==========================================================
import httplib
import re
import time
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element


def getURLs(content):
	result_re=re.compile('<a.+href="(/html/.+html)">')
	result=result_re.findall(content)
	return result
	
def getPages(context, pageURL):
	context.request('GET',pageURL)
	content=context.getresponse()
	if content.status!=200:
		print 'http error:',content.status
		exit(-1)
	return content.read()
	
def getTitles(content):
	title=re.findall('<a.+href="/html/.+html">(.+)</a>',content)
	return title

def check_updated(url, latest_url):
	return (url==latest_url)

def do_update(urls, titles, latest_url, xml_file):
	try:
		tree=ET.parse("/s/test/"+xml_file)
	except:
		f = open("/s/test/"+xml_file,"w")
		f.close()
		tree=ET.parse("/s/test/"+xml_file)
	root=tree.getroot()
	channel=root.find('channel')
	latest_update=latest_url
	for new_item in getNewItems(urls,titles,latest_url):
		channel.insert(3,create_item(new_item[0],unicode(new_item[1],'utf8')))
		latest_update=new_item[0]
	tree.write("/s/test/"+xml_file)
	return latest_update

def create_item(url, title):
	element_item = Element('item')
	element_title = Element('title')
	element_link = Element('link')
	element_description=Element('description')
	element_title.text=title
	element_link.text=url
	element_description.text=title
	element_item.insert(0,element_description)
	element_item.insert(0,element_link)
	element_item.insert(0,element_title)
	return element_item

def getNewItems(urls, titles, latest_url):
	newItems=[]
	for i in range(len(urls)):
		if urls[i] == latest_url:
			break
		else:
			newItems.append((urls[i],titles[i]))
	print newItems[0][1]
	newItems.reverse()
	return newItems
	
def up():
	Ver = int(time.time())
	isnew = False
	page_set=[
		'/html/kydt/all/page1',
		'/html/xwzx/xyxw/page1',
		'/html/bksjx/all/page1',
		'/html/yjsjx/all/page1',
		'/html/xsgz/all/page1',
		'/html/zsxx/all/page1'
	]#���ж�̬��ѧԺ���ţ��������������о���������ѧ��������������ѧ
	xml_set=[
		'kydt.xml',
		'xwzx.xml',
		'bksjx.xml',
		'yjsjx.xml',
		'xsgz.xml',
		'zsxx.xml'
	]

	file=open('/s/test/latest','r')
	latest=file.read()
	file.close()
	New = []
	st = ""
	for i in range(len(latest)):
		if latest[i] != "\n":
			st += latest[i]
		else:
			New.append(st)
			st = ""
	latest = New[:]
	print latest
	conn=httplib.HTTPConnection('sms.nankai.edu.cn')
	for i in range(len(page_set)):
		page=getPages(conn, page_set[i])
		urls=getURLs(page)
		titles=getTitles(page)
		if not check_updated(urls[0], latest[i]):
			latest_update=do_update(urls, titles, latest[i], xml_set[i])
			latest[i]=latest_update
			isnew = True
	conn.close()
	f = open("/s/test/"+"Now","w")
	f.write(str(Ver))
	f.close()
	if isnew:
		file=open("/s/test/"+'latest','w')
		for line in latest:
			file.write(str(line))
			file.write("\n")
		file.close()
		f = open("/s/test/"+"Version","w")
		f.write(str(Ver))
		f.close()
	return(QAQ.app3)
if __name__ == "__main__":
	up()