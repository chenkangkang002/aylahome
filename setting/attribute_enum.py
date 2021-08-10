#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：aylahome 
@File    ：attribute_enum.py
@IDE     ：PyCharm 
@Author  ：陈康
@Date    ：2021/6/8 23:15 
'''
import enum

class DeviceAttribute(enum.Enum):
    #风速
    S1 = '低速'
    S2 = '中速'
    S3 = '高速'
    S4 = '自动'
    #空调模式
    M1 = '制冷'
    M2 = '制热'
    M3 = '送风'
    M4 = '除湿'
    #打开/关闭
    K1 = 'ON'
    K2 = 'OFF'
    #对应属性值转换
    ON = '1'
    OFF = '0'

    #对应的diviceName对应的验证function名称


    @classmethod
    def get_all_name(self):
        name_list = []
        for c in self.__members__.items():
            name_list.append(c[0])
        return name_list
