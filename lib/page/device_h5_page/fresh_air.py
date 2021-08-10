#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：aylahome 
@File    ：fresh_air.py    新风
@IDE     ：PyCharm 
@Author  ：陈康
@Date    ：2021/6/3 16:39 
'''
from selenium.webdriver.common.by import By

from lib.page.base_page import BasePage


class FreshAir(BasePage):

    loc_PowerSwitch =  (By.XPATH,'//android.view.View/android.view.View[2]/android.view.View[6]/android.view.View[3]/android.widget.Image')#开关按钮
    loc_PowerSwitch_on = (By.XPATH,'//android.view.View/android.view.View[2]/android.view.View[6]/android.view.View[1]')  #开关打开on
    loc_PowerSwitch_off = (By.XPATH, '//android.view.View/android.view.View[2]/android.view.View[6]/android.view.View[2]')  # 开关打开off
    loc_offline_status = (By.XPATH, '//android.view.View/android.view.View[2]/android.view.View[2]/android.view.View')    #在离线状态

    # {"propertyCode":"PowerSwitch","propertyValue":0}    #开关关闭 0-1
    # {"propertyCode":"WindSpeed","propertyValue":3}  #风速中速 2-3-4



