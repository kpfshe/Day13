# -*- coding utf-8 -*-
# author：zhanghuimin
import xlrd
from xlutils.copy import copy
from FiveTest.Day13.utils import public
from FiveTest.Day13.utils import excelEnum

class OperateExcel:

	def getExcel(self,num=0):
		'''获取到指定文件指定的sheet对象,使用函数的默认参数'''
		db = xlrd.open_workbook(public.base_dir('data', 'data.xls'))
		sheet = db.sheet_by_index(num)
		return sheet

	def get_rows(self):
		'''获取指定sheet的所有行数'''
		return self.getExcel().nrows

	def get_cellValue(self,row,col):
		'''获取单元格的具体内容'''
		return self.getExcel().cell_value(row,col)

	def get_url(self,row):
		'''获取excel中请求地址'''
		return self.get_cellValue(row,excelEnum.getURL())

	def get_data(self,row):
		'''获取excel中请求参数'''
		return self.get_cellValue(row,excelEnum.getData())

	def get_expect_result(self,row):
		'''获取excel中期望结果'''
		return self.get_cellValue(row,excelEnum.getExpectResult())

	def get_actual_result(self,row):
		'''获取excel中实际结果'''
		return self.get_cellValue(row,excelEnum.getActualResult())

	def getHeaders(self):
		'''获取请求头'''
		headers ={
			'Content-Type':'application/x-www-form-urlencoded',
			'Cookie':'LGUID=20170706155132-ed28a4f8-621f-11e7-aa05-525400f775ce; _ga=GA1.2.2011161793.1517908820; user_trace_token=20180820113257-bb066b7d-a429-11e8-94d4-525400f775ce; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22166a5d38fb4d65-059eaac36b860d-b79193d-921600-166a5d38fb5d9%22%2C%22%24device_id%22%3A%22166a5d38fb4d65-059eaac36b860d-b79193d-921600-166a5d38fb5d9%22%7D; LG_LOGIN_USER_ID=5f763cb60a03d88d60769cc5206d07ef4d2ff47d4297ff0f; index_location_city=%E5%8C%97%E4%BA%AC; WEBTJ-ID=20181107175510-166ed98df76639-0916f964e4985b-b79183d-921600-166ed98df78552; _gat=1; LGSID=20181107175511-3737df00-e273-11e8-9046-525400f775ce; PRE_UTM=m_cf_cpt_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3Dlagou%26rsv_spt%3D1%26rsv_iqid%3D0xb8aeadee00052e38%26issp%3D1%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D2%26ie%3Dutf-8%26tn%3Dbaiduhome_pg%26rsv_enter%3D1%26rsv_sug3%3D4%26rsv_sug1%3D4%26rsv_sug7%3D100; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flp%2Fhtml%2Fcommon.html%3Futm_source%3Dm_cf_cpt_baidu_pc; _gid=GA1.2.685952360.1541584511; JSESSIONID=ABAAABAAAFCAAEG7797B813DA0FD69836A109B8FF679FF1; LGRID=20181107175514-39886877-e273-11e8-9046-525400f775ce; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1540381067,1540455278,1541584511,1541584515; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1541584515; TG-TRACK-CODE=index_search; SEARCH_ID=65ef3104e8d14a46b6c603f36c94025f',
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
			'Referer':'https://www.lagou.com/jobs/list_%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95?labelWords=&fromSearch=true&suginput='
		}
		return headers

	def writeResult(self,row,col,content):
		'''将执行成功的用例写入PASS到excel中'''
		db = xlrd.open_workbook(public.base_dir('data','data.xls'))
		old_content = copy(db)
		old_content.get_sheet(0).write(row,col,content)
		old_content.save(public.base_dir('data','data.xls'))

	def getSuccessCase(self):
		'''获取执行成功的用例数，即统计excel中实际结果为pass的条数'''
		success_count = 0
		for i in range(1,self.get_rows()):
			if self.get_actual_result(i) == 'PASS':
				success_count = success_count+1

		return success_count

	def getFailCase(self):
		'''获取执行失败的用例数'''
		fail_count = self.get_rows()-1-self.getSuccessCase()

		return fail_count

	def runPassRate(self):
		'''计算执行成功的通过率,并且保留两位小数'''
		rate = ''
		if self.getFailCase()==0:
			rate = '100%'
		else:
			rate = str(round(self.getSuccessCase()/(self.get_rows()-1),2)*100)+'%'

		return rate

