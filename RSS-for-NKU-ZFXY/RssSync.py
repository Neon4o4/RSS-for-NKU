#encoding=utf8
#==========================================================
#getPages():  根据链接获取网页内容
#getURLs():  从网页内容中获取新闻的链接
#getTitles():  从网页内容中获取新闻的标题
#check_updated():  检查某个新闻分类是否有更新
#do_update():  更新某个新闻分类的XML文件
#creat_item():  根据新闻链接和标题创建XML格式的新闻内容节点
#getNewItems():  根据有更新的内容创建XML格式的新闻节点
#==========================================================
import httplib
import re
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element

def getURLs(content):
	result_re=re.compile('<a[\s]{,3}href="(/newsview/[/0-9a-zA-Z\-]+)"')
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
	title=re.findall(u'<span class="newsTitle.+?">([\s\S]+?)</span>',unicode(content,'utf8'))
	for t in title:
		t=re.sub('<b>','',unicode(t))
		t=re.sub('</b>','',unicode(t))
		#print t
	return title

def check_updated(url, latest_url):
	return (url==latest_url)

def do_update(urls, titles, latest_url, xml_file):
	tree=ET.parse(xml_file)
	root=tree.getroot()
	channel=root.find('channel')
	latest_update=latest_url
	for new_item in getNewItems(urls,titles,latest_url):
		channel.insert(3,create_item(new_item[0],new_item[1]))
		latest_update=new_item[0]
	tree.write(xml_file)
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
	
if __name__ == '__main__':
	page_set=[
		'/news/anounce',
		'/news/bachelor',
		'/news/postgraduate',
		'/news/master',
		'/news/league',
		'/news/scholar-research',
		'/news/admission-job'
	]#综合信息，本科生教育，研究生教育，专业学位，团学活动，科研信息，招生就业
	xml_set=[
		'anounce.xml',
		'bachelor.xml',
		'postgraduate.xml',
		'master.xml',
		'league.xml',
		'scholar-research.xml',
		'admission-job.xml'
	]

	file=open('latest','r')
	latest=file.readlines()
	file.close()
	for i in range(len(latest)):
		latest[i]=latest[i].strip('\n')
	#print latest
	conn=httplib.HTTPConnection('zfxy.nankai.edu.cn')
	for i in range(len(page_set)):
		page=getPages(conn, page_set[i])
		#print page
		urls=getURLs(page)
		titles=getTitles(page)
		#print len(urls)
		#print len(titles)
		if not check_updated(urls[0], latest[i]):
			latest_update=do_update(urls, titles, latest[i], xml_set[i])
			latest[i]=latest_update
	conn.close()
	
	file=open('latest','w')
	file.truncate()
	for line in latest:
		file.writelines(line+'\n')
	file.close()
