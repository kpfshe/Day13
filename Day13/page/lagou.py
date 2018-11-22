# -*- coding utf-8 -*-
# author：zhanghuimin

from FiveTest.Day13.utils.operateJson import OperateJson
from FiveTest.Day13.utils.public import base_dir
import json

operate = OperateJson()

def setVariable(row,data):
	'''得到要修改的字典，修改后返回该字典'''
	variable = operate.get_request_data(row)
	variable['kd']=data
	return variable

def writePositionId(positionIds):
	'''将请求获取到的positionId写入到文件'''
	with open(base_dir('data','positionId'),'w') as f:
		f.write(positionIds)

def getPositionId():
	'''将文件中的positionIsds读取出来'''
	with open(base_dir('data','positionId'),'r') as f:
		return json.loads(f .read())

def setUrl(i):
	'''将positionId动态的传入url中'''
	url = 'https://www.lagou.com/jobs/{0}.html'.format(getPositionId()[i])
	return url


def setPositionId(row,i):
	'''设置positionId的内容'''
	variable = operate.get_request_data(row)
	variable['positionId']=getPositionId()[i]
	return variable



