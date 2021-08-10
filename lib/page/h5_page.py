#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：aylahome 
@File    ：h5_page.py
@IDE     ：PyCharm 
@Author  ：陈康
@Date    ：2021/5/17 18:35 
'''
from selenium.webdriver.common.by import By

from lib.page.base_page import BasePage


class H5Page(BasePage):

    loc_h5_device_name = (By.CLASS_NAME, 'nav-bar__title') #单控页的设备名称
    loc_app = 'app'  # 定位H5页面中的App位置
    loc_back_01 = '//android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View' #相对于id为app的元素的xpath
    loc_back_02 = '//android.view.View/android.view.View[1]/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View/android.view.View'
    loc_back = (By.CLASS_NAME, 'nav-bar__icon van-icon van-icon-arrow-left')    #H5返回按钮classname

    def get_h5_device_name(self,deviceName):
        '''获取单控页中设备的名称'''
        return  self.get_element_text(deviceName, type=1).text

    def click_back_but(self,deviceName=None):
        '''点击返回按钮< '''
        # self.get_element(self.loc_back).click()
        deveices = ["罗马红外人体传感器","罗马紧急按钮开关","罗马水地暖面板","罗马水地暖面板","米兰触控面板S1"]
        if deviceName != None and deviceName in deveices:
            self.get_element_resourceId(self.loc_app).find_element_by_xpath(self.loc_back_02).click()
        else:
            self.get_element_resourceId(self.loc_app).find_element_by_xpath(self.loc_back_01).click()
