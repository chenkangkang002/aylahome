#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：aylahome 
@File    ：more_and_more.py 更多页面
@IDE     ：PyCharm 
@Author  ：陈康
@Date    ：2021/7/27 23:38 
'''
from selenium.webdriver.common.by import By

from lib.page.base_page import BasePage


class MoreAndMore(BasePage):

    loc_curtain_nickname = (By.ID, 'com.ayla.aylahome:id/ui_rl_nickname')   #双路窗帘开关名称命名入口
    loc_curtain_name1 = (By.ID, 'com.ayla.aylahome:id/sr_et_name1')   #窗帘一的输入框
    loc_curtain_name2 = (By.ID, 'com.ayla.aylahome:id/sr_et_name2')   #窗帘二的输入框
    loc_name_save = (By.ID, 'com.ayla.aylahome:id/sr_btn_save')     #窗帘一二的名称保存按钮
    loc_back = (By.ID, 'com.ayla.aylahome:id/mLeftIv')   #返回按钮

    def click_curtain_nickname(self):
        '''点击双路窗帘开关的开关命名入口'''
        self.get_element(self.loc_curtain_nickname).click()

    def input_curtain_name1(self, name1):
        '''输入窗帘一的名称'''
        ele = self.get_element(self.loc_curtain_name1)
        ele.clear()
        ele.send_keys(name1)

    def input_curtain_name2(self, name2):
        '''输入窗帘二的名称'''
        ele = self.get_element(self.loc_curtain_name2)
        ele.clear()
        ele.send_keys(name2)

    def click_name_save(self):
        '''点击窗帘一二的名称保存按钮'''
        self.get_element(self.loc_name_save).click()

    def click_back(self):
        '''点击返回按钮'''
        self.get_element(self.loc_back).click()

    #业务方法
    def curtain_nickname(self, name1, name2):
        '''双路窗帘开关命令'''
        self.click_curtain_nickname()
        self.input_curtain_name1(name1)
        self.input_curtain_name2(name2)
        self.click_name_save()
        self.click_back()
