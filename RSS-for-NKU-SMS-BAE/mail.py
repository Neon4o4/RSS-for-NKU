from sae.mail import EmailMessage
ToList = ["446709220@qq.com"]
def send_mail(HTML):
	m = EmailMessage()
	m.to = ToList
	m.subject = "Update"
	m.html = HTML
	m.smtp = ('smtp.qq.com', 25, '2034393074@qq.com', '13326518308', False)
	m.send()