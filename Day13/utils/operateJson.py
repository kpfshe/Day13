# -*- coding utf-8 -*-
# author：zhanghuimin
from FiveTest.Day13.utils.public import base_dir
import json
from FiveTest.Day13.utils.operateExcel import *

class OperateJson:
	'''在类的构造函数将需要调用的类进行实例化，实际效果相当于继承类'''
	def __init__(self):
		self.excel = OperateExcel()

	def getReadJson(self):
		'''使用文件的反序列化将某个json文件的内容读取出来'''
		return json.load(open(base_dir('data','requestData.json'),'r',encoding='utf-8'))
	''' 获取具体key的value值'''
	def get_request_data(self,row):
		return self.getReadJson()[self.excel.get_data(row)]

# op = OperateJson()
# print(op.get_request_data(1))


