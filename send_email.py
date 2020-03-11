import smtplib
import config

def alert(subject,message):
	try:
		server=smtplib.SMTP('smtp.gmail.com:587')
		server.ehlo()
		server.starttls()
		server.login(config.EMAIL,config.PASS)
		msg='{}\n{}'.format(subject,message)
		server.sendmail(config.EMAIL,config.EMAIL2,msg)
		server.quit()
	except:
		print("Error")


sub="test"
mes="message"
alert(sub,mes)
