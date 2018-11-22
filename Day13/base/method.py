# -*- coding utf-8 -*-
# author：zhanghuimin
'''python没有方法的重载，想要实现重载的功能只能使用默认函数来实现'''
import requests
from FiveTest.Day13.utils.operateJson import *
from FiveTest.Day13.page import lagou

class Method:
	def __init__(self):
		self.excel= OperateExcel()
		self.json = OperateJson()

	def get(self,url,params=None):
		r = requests.get(url=url,headers=self.json.excel.getHeaders(),timeout=6)
		return r

	def post(self,row,data=None):
		try:
			r = requests.post(url=self.json.excel.get_url(row),
			                  headers=self.json.excel.getHeaders(),
			                  data=self.json.get_request_data(row),
			                  timeout=6)
			return r
		except Exception:
			raise RuntimeError('接口请求异常')

	def post1(self,row,data):
		try:
			r = requests.post(url=self.json.excel.get_url(row),
			                  headers=self.json.excel.getHeaders(),
			                  data=data,
			                  timeout=6)
			return r
		except Exception:
			raise RuntimeError('接口请求异常')


