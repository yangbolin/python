#!/usr/bin/python
#FileName:send-emial.py 
#send email

import sys
import time
import email
import smtplib

def send_mail():
	try:
		handle = smtplib.SMTP('smtp.126.com',25)
		handle.login('nuaa_ybl@126.com','Hello890826')
		msg = 'To: boris.yangbl@alibaba-inc.com\r\nFrom:nuaa_ybl@126.com\r\nSubject:hello yangbolin\r\n'
		handle.sendmail('nuaa_ybl@126.com','nuaa_ybl@126.com', msg)     
		handle.close()
		print 'Send Email Successfully!'
		return 1
	except:
		print 'Send Email Failure!'
		return 0
if __name__ == "__main__":
	print __name__
	send_mail()
