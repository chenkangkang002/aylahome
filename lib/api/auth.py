#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：testgrouppub 
@File    ：auth.py
@IDE     ：PyCharm 
@Author  ：陈康
@Date    ：2021/5/6 14:27 
'''
import requests
from setting.variament import *

def get_home_info():
    '''
    获取账号下的家庭信息列表:[{home1},{home2},{home3}]
    '''
    url = HOST + HOME_URL
    headers = {'Authorization' : TOKEN}
    return requests.get(url = url, headers = headers).json()['data']

def get_device_list(home_name = HOME_NAME):
    # homeId = find_specified_homeId(home_name)
    home_list = get_home_info()
    homeId = None
    for var in home_list:
        if home_name == var['homeName']:
            homeId = var['homeId']
    url = HOST + DEVICE_LIST_URL
    headers = {'Authorization': TOKEN}
    requestBody = {"roomId": homeId,"pageNo":1,"pageSize":500}
    return requests.post(url=url, headers=headers, json = requestBody).json()['data']['devices']

def get_device_h5_properties(deviceId, type=0):
    '''
    获取设备的H5属性
    :param deviceId: 设备ID
    :param type: 设备类型，0：正常设备，1：用途设备
    :return:
    '''
    url = None
    if type == 0:
        url = HOST_H5 + PROPERTIES_URL.format(deviceId)
    elif type == 1:
        url = HOST_H5 + USE_DEVICE_PROPERTY_URL.format(deviceId)
    headers = {'Authorization': TOKEN}
    return requests.get(url=url, headers=headers).json()['data']
