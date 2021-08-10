#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：testgrouppub 
@File    ：conftest1.py
@IDE     ：PyCharm 
@Author  ：陈康
@Date    ：2021/4/29 19:00 
'''
import os

import pytest
from appium import webdriver


@pytest.fixture(scope="session",autouse=True)
def getDriverAndroid():
    '''打开Android端的连接'''
    #另外一个手机：b313d9f0
    #施工
    #com.ayla.hotelsaas/.ui.SPlashActivity
    # 艾拉
    #com.ayla.aylahome/com.ayla.user.ui.SplashActivity
    desired_capabilities = {    #真机
        'platformName': 'Android',
        'platformVersion': '11',
        'deviceName': 'e012a6a1',   #oppo:e012a6a1,vivo:b313d9f0
        'appPackage': 'com.ayla.aylahome',
        'appActivity': 'com.ayla.user.ui.SplashActivity',
        'noReset': True
    }
    # desired_capabilities = {  #模拟器genymotion
    #     'platformName': 'Android',
    #     'platformVersion': '8.1',
    #     'deviceName': '192.168.138.103:5555',  #
    #     'appPackage': 'com.ayla.aylahome',
    #     'appActivity': 'com.ayla.user.ui.SplashActivity',
    #     'noReset': True,
    #     'chromeOptions': {'androidProcess': 'com.ayla.aylahome'}
    # }
    # driver = webdriver.Remote(desired_capabilities = desired_capabilities)
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
    driver.implicitly_wait(10)
    print('获取到driver')
    yield driver
    print('关闭driver')
    #执行完之后生成测试报告
    command = 'allure generate allure/allure_result -o allure/allure_report --clean'
    os.system(command)

@pytest.fixture()
def getDriver(getDriverAndroid):
    print('每个方法从总的session中获取driver')
    yield getDriverAndroid