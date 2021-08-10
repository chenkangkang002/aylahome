#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：aylahome 
@File    ：validation_h5.py
@IDE     ：PyCharm 
@Author  ：陈康
@Date    ：2021/6/16 15:43 
'''
from time import sleep

import allure

from func.utils import find_h5_device_property
from lib.page.base_page import BasePage
from lib.page.device_h5_page.the_curtain import TheCurtain
from lib.page.h5_page import H5Page
from lib.page.more_and_more import MoreAndMore
from setting.attribute_enum import DeviceAttribute
from setting.variament import DOUBLE_CURTAIN_NAME


class ValidationH5(BasePage):
    '''验证H5'''
    def __init__(self,driver):
        super().__init__(driver)
        self._operator_map = {
            '灯': self.use_devices,
            '空调': self.air_conditioning,
            '地暖': self.floor_heating,
            '新风': self.fresh_air,
            '窗帘': self.fresh_air,
        }

    def switch_validation_function(self, **kwargs):
        '''根据deviceName选择验证H5的方法'''
        fun = None
        device_name = kwargs['deviceName']
        for device in self._operator_map.keys():
            if device in device_name:
                fun = self._operator_map.get(device)
                break
        if fun is not None:
            fun(**kwargs)

    def curtain(self, **kwargs):
        '''验证窗帘类设备'''
        deviceName = kwargs['deviceName']
        nickname = kwargs['nickname']
        deviceId = kwargs['deviceId']
        properties = {}
        tc = TheCurtain(self.driver)
        if '二路' in deviceName:
            tc.click_more()
            mam = MoreAndMore(self.driver)  #H5页面点击更多【...】
            mam.curtain_nickname(DOUBLE_CURTAIN_NAME[0],DOUBLE_CURTAIN_NAME[-1])    #给两个窗帘命名
            with allure.step('断言是否命名成功'):
                assert self.get_index_device(DOUBLE_CURTAIN_NAME[0])
                assert self.get_index_device(DOUBLE_CURTAIN_NAME[-1])
            tc.switch_curtain(DOUBLE_CURTAIN_NAME[0])
            tc.click_double_curtain_on()
            tc.switch_curtain(DOUBLE_CURTAIN_NAME[-1])
            tc.click_double_curtain_off()
            properties = {'deviceId': deviceId, 'type': 0,
                          'data': [
                              {'propertyName': 'CurtainOperation_1', 'propertyValue': '1'},  # 窗帘一打开
                              {'propertyName': 'CurtainOperation_2', 'propertyValue': '0'},  # 窗帘二关闭
                          ]
                          }
        else:
            properties = {'deviceId': deviceId, 'type': 0,
                          'data': [
                              {'propertyName': 'CurtainOperation', 'propertyValue': '1'},  # 窗帘打开
                          ]
                          }

        self.screenshot(nickname)
        with allure.step('返回设备列表'):
            self.swipe_back_index()
            sleep(0.5)
        assert find_h5_device_property(**properties)

    def use_devices(self,**kwargs):
        '''
        验证用途(灯：开关)、插座类设备
        :param value: 开关K1=ON,K2=OFF
        :param deviceId: 设备ID
        :param property: 属性名称
        :param type: 设备的类型0：正常设备，1：用途设备
        :return:
        '''
        value = 'K1'  #kwargs['value']
        deviceId = kwargs['deviceId']
        # property = kwargs['property']
        type = 0    #kwargs['type']
        self.switch_on_off(value)
        sleep(1)
        assert self.get_index_device(DeviceAttribute[value].value)
        nickname = kwargs['nickname']  # '罗马电地暖'
        deviceName = kwargs['deviceName']
        self.screenshot(nickname)
        hp = H5Page(self.driver)
        with allure.step('返回设备列表'):
            self.swipe_back_index()
            sleep(0.5)
        properties = {'deviceId': deviceId, 'type': 0,
                      'data': [
                          {'propertyName': '232:0x0201:ACSwitch', 'propertyValue': '1'},  # 开关打开
                          {'propertyName': '232:0x0202:FanMode', 'propertyValue': '2'},  # 风速中档
                          {'propertyName': '32:0x0201:SysMode', 'propertyValue': '7'},  # 模式送风
                      ]
                      }
        # propertyValue = find_h5_device_property(**properties)
        assert find_h5_device_property(**properties)

    def air_conditioning(self, **kwargs):
        '''
        验证空调类设备，控制模式、风速、温度
        对于空调设备：
        1、打开开关
        2、改变风速
        3、修改模式
        4、修改温度（增加或者降低，但是要考虑到最大温度和最小温度的情况）
        :param kwargs:
        :return:
        '''
        # value = kwargs['value']
        type = 0 #kwargs['type']
        deviceId = kwargs['deviceId']
        # property = kwargs['property']

        #打开开关
        value_1 = 'K1'
        self.switch_on_off(value_1)
        sleep(0.5)
        # 2、改变风速
        value_2 = 'S2'
        self.switch_wind_speed_or_model(value_2, type)
        sleep(0.5)
        # 3、修改模式
        value_3 = 'M3'
        self.switch_wind_speed_or_model(value_3, type)
        sleep(0.5)
        # 4、修改温度

        sleep(1)
        assert self.get_index_device(DeviceAttribute[value_1].value)
        assert self.get_index_device(DeviceAttribute[value_2].value)
        assert self.get_index_device(DeviceAttribute[value_3].value)
        nickname = kwargs['nickname']  # '罗马电地暖'
        deviceName = kwargs['deviceName']
        self.screenshot(nickname)
        hp = H5Page(self.driver)
        with allure.step('返回设备列表'):
            self.swipe_back_index()
            sleep(0.5)
        properties = {'deviceId': deviceId, 'type': 0,
                      'data': [
                          {'propertyName': '232:0x0201:ACSwitch', 'propertyValue': '1'},   #开关打开
                          {'propertyName': '232:0x0202:FanMode', 'propertyValue': '2'},  # 风速中档
                          {'propertyName': '32:0x0201:SysMode', 'propertyValue': '7'},  # 模式送风
                      ]
                      }
        # propertyValue = find_h5_device_property(**properties)
        assert find_h5_device_property(**properties)

    def fresh_air(self, **kwargs):
        '''验证新风类设备,控制风速'''
        value = kwargs['value']
        type = kwargs['type']
        deviceId = kwargs['deviceId']
        property = kwargs['property']
        self.switch_wind_speed_or_model(value, type)
        sleep(1)
        assert self.get_index_device(value)
        propertyValue = find_h5_device_property(deviceId=deviceId, property=property, type=type)
        assert DeviceAttribute[DeviceAttribute[value].value].value == propertyValue

    def floor_heating(self, **kwargs):
        '''验证地暖类设备，控制温度'''
        value = kwargs['value']
        type = kwargs['type']
        deviceId = kwargs['deviceId']
        property = kwargs['property']
        self.switch_wind_speed_or_model(value, type)
        sleep(1)
        assert self.get_index_device(value)
        propertyValue = find_h5_device_property(deviceId=deviceId, property=property, type=type)
        assert DeviceAttribute[DeviceAttribute[value].value].value == propertyValue

    def sensor(sel, **kwargs):
        '''验证传感器类设备'''