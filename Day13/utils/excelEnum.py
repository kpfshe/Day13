# -*- coding utf-8 -*-
# author：zhanghuimin
class ExcelEnum:
	CaseID=0
	Description=1
	URL=2
	data=3
	ExpectResult=4
	ActualResult=5

def getCaseID():
	return ExcelEnum.CaseID

def getDescription():
	return ExcelEnum.Description

def getURL():
	return ExcelEnum.URL

def getData():
	return ExcelEnum.data

def getExpectResult():
	return ExcelEnum.ExpectResult

def getActualResult():
	return ExcelEnum.ActualResult




