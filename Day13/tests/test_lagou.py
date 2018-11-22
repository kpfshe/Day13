# -*- coding utf-8 -*-
# author：zhanghuimin
import unittest
from FiveTest.Day13.base.method import Method
from FiveTest.Day13.utils.operateExcel import *
from FiveTest.Day13.page import lagou
import json
from FiveTest.Day13.utils.excelEnum import *

class LagouTest(unittest.TestCase):

	def setUp(self):
		self.obj = Method()
		self.excel = OperateExcel()
		self.enum = ExcelEnum()

	def statusCode(self,r):
		'''断言协议状态码为200'''
		self.assertEqual(r.status_code,200)
		'''断言业务状态码为0'''
		self.assertEqual(r.json()['code'],0)

	def test_lagou_001(self):
		'''拉勾---验证搜索关键字为excel中填写的’'''
		r = self.obj.post(row=1)
		self.statusCode(r)
		self.assertIn(self.excel.get_expect_result(1),r.text)
		self.excel.writeResult(row=1,col=self.enum.ActualResult,content='PASS')

	def test_lagou_002(self):
		'''拉勾---测试变换搜索职位名称'''
		r = self.obj.post(row=1,data=lagou.setVariable(row=1,data='性能测试工程师'))
		self.statusCode(r)
		self.assertIn(self.excel.get_expect_result(1),r.text)

	def test_lagou_003(self):
		'''拉勾---测试将搜索到的positionId写入文件'''
		r = self.obj.post(row=1,data=lagou.setVariable(row=1,data='性能测试工程师'))
		self.statusCode(r)
		positionIds = []
		for i in range(0,15):
			positionId = r.json()['content']['positionResult']['result'][i]['positionId']
			positionIds.append(positionId)

		lagou.writePositionId(json.dumps(positionIds))

	def test_lagou_004(self):
		'''测试查看关键字为‘性能测试工程师’的第一页的第一个职位信息'''
		r = self.obj.get(url=lagou.setUrl(0))
		self.assertEqual(r.status_code,200)
		#self.assertIn(self.excel.get_expect_result(2),r.text)
		#print(r.text)
		self.excel.writeResult(row=2,col=self.enum.ActualResult,content='PASS')


# if __name__=='__main__':
# 	suite = unittest.makeSuite(LagouTest)
# 	unittest.TextTestRunner(verbosity=2).run(suite)
