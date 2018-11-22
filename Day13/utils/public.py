# -*- coding utf-8 -*-
# author：zhanghuimin
import os
'''找到各目录下的具体文件'''
def base_dir(dirname,filename):
	return os.path.join(os.path.dirname(os.path.dirname(__file__)),dirname,filename)

