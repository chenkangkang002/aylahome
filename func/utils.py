#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：testgrouppub 
@File    ：utils.py
@IDE     ：PyCharm 
@Author  ：陈康
@Date    ：2021/4/29 19:02 
'''
from lib.api.auth import get_home_info, get_device_list, get_device_h5_properties
from setting.variament import H5_DEVICE


def find_specified_homeId(home_name):
    '''获得指定家庭的homeId'''
    home_list = get_home_info()
    for var in home_list:
        if home_name == var['homeName']:
            return var['homeId']

def find_specified_device_info(home_name, device_name):
    '''获得指定设备的信息{deviceId:11,deviceName:ww……}'''
    device_list = get_device_list(home_name)
    for var in device_list:
        if var['deviceName'] == device_name or var['nickname'] == device_name:
            return var
    return False    #不存在指定的设备

def find_device_h5_specified_property(deviceId,property_name=None):
    '''获得指定设备的H5指定属性或全部属性'''
    property_list = get_device_h5_properties(deviceId)
    if property_name == None:
        return property_list
    else:
        for var in property_list:
            if var['propertyName'] == property_name:
                return var
        return False    #f'该设备不存在属性：{property_name},或输入属性错误'

def find_index_device_list():
    '''获取首页设备列表，这里不包含用途设备的主设备："deviceUseType": 3的'''
    device_list = get_device_list()
    new_device_list = []
    for var in device_list:
        if var['deviceUseType'] != 3:
            if H5_DEVICE != [] and var['nickname'] in H5_DEVICE:
                new_device_list.append(var)
            elif H5_DEVICE == []:
                new_device_list.append(var)
    return new_device_list

def judge_data_to_deviceLinkage(scene_info):
    '''判断设备联动的数据有效性'''
    if isinstance(scene_info,dict):
        if 'conditions' not in scene_info.keys():
            raise KeyError('不存在key:conditions')
        if 'actions' not in scene_info.keys():
            raise KeyError('不存在key:actions')
        if scene_info['conditions'] == [] or scene_info['conditions'] == None:
            raise ValueError("conditions为空")
        if scene_info['actions'] == [] or scene_info['actions'] == None:
            raise ValueError("actions为空")
    else:
        raise TypeError('设备联动数据应该为dict类型')

# def switch_h5_model(driver):
#     '''进入H5,切换到H5模式'''
#     contexts = driver.contexts
#     if len(contexts)>1 and
#     driver.switch_to.context(contexts[-1])
#     return driver.page_source

def find_h5_device_property(**kwargs):
    '''
    根据设备ID和设备的属性名称获取到设备的属性值
    {'deviceId':v,'type':v,'data':[{'propertyName':v,'propertyValue':v}]}
    :param deviceId: 设备ID
    :param property: 设备的属性
    :param type:设备的类型，0：正常设备，1：用途设备
    :param data: list，[{'propertyName':v,'propertyValue':v}]存放了被操作的属性的列表，包含propertyName，propertyValue，
    :return: propertyValue
    '''
    deviceId = kwargs['deviceId']
    type = kwargs['type']
    datas = kwargs['data']
    print(kwargs)
    properties = get_device_h5_properties(deviceId,type)
    lis = []
    count = len(datas)
    ret = False
    for d in datas:
        for var in properties:
            var = str(var).replace(' ','').replace("':'",'=')
            if d['propertyName'] in var and d['propertyValue'] in var :
                lis.append(True)
    if len(lis) == count:
        ret = True
    return ret