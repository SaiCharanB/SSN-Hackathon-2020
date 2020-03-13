import smtplib
import config
from email.message import EmailMessage

def alert(subject,message):
	try:
		server=smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		msg=EmailMessage()
		server.login(config.EMAIL,config.PASS)
		msg.set_content(message)
		msg['Subject']=subject
		msg['From']=config.EMAIL
		msg['To']=config.EMAIL2
		server.send_message(msg)
		server.quit()
	except:
		print("Error")


sub="ALERT"
mes="Intruder"
alert(sub,mes)
