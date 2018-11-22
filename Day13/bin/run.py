# -*- coding utf-8 -*-
# author：zhanghuimin
import unittest
from FiveTest.Day13.utils.public import base_dir
from FiveTest.Day13.utils.operateExcel import OperateExcel
import smtplib
from email.mime.text import MIMEText
import os

class Run:
	def __init__(self):
		self.excel = OperateExcel()

	def getSuite(self):
		'''获取要执行的测试用例'''
		base_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)),'tests')
		suite = unittest.TestLoader().discover(start_dir=base_dir,
		                                     pattern='test_*.py',
		                                     top_level_dir=None)
		return suite

	def send_mail(self,to_user,sub,content):
		'''
		发送测试结果到指定的邮件，邮箱的登录密码是在网易中开启授权码登录设置的授权密码，不是登录邮箱的密码
		:param to_user:接受邮件的账户
		:param sub:邮件主题
		:param content:邮件内容
		'''
		global send_mail
		global send_user
		send_mail = "smtp.163.com"
		send_user = "kpfshe@163.com"
		message = MIMEText(content,_subtype='plain',_charset='utf-8')
		message['Subject']=sub
		message['From']=send_user
		message['To']=to_user
		server = smtplib.SMTP()
		server.connect(send_mail)
		server.login(send_user,'118NIHAO')
		server.sendmail(send_user,to_user,message.as_string())
		server.close()

	def main_run(self):
		'''批量执行测试用例'''
		unittest.TextTestRunner(verbosity=2).run(self.getSuite())
		sub='2018-11-14测试拉勾网结果'
		content='通过数;{0} 失败数：{1} 通过率：{2}'.format(self.excel.getSuccessCase(),self.excel.getFailCase(),self.excel.runPassRate())
		print('Please wait while the statistics test result are send to the email')
		self.send_mail('1959451013@qq.com',sub,content)

if __name__=='__main__':
	Run().main_run()





