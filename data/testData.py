#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：aylahome 
@File    ：testData.py
@IDE     ：PyCharm 
@Author  ：陈康
@Date    ：2021/5/26 15:50 
'''
from func.utils import find_index_device_list

DEVICE_LIST_DATA = find_index_device_list() #首页设备列表遍历数据
print(DEVICE_LIST_DATA)