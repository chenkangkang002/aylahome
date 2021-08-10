#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：aylahome 
@File    ：the_curtain.py    窗帘
@IDE     ：PyCharm 
@Author  ：陈康
@Date    ：2021/7/27 22:23 
'''
from lib.page.base_page import BasePage


class TheCurtain(BasePage):

    loc_app = 'app'
    loc_double_curtain_on = '//android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[4]'    #双路窗帘打开
    loc_double_curtain_suspended = '//android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[5]'  # 双路窗帘暂停
    loc_double_curtain_off = '//android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[6]'    #双路窗帘关闭
    loc_one_curtain_on = '//android.view.View/android.view.View[2]/android.view.View[4]/android.view.View[1]' #一路窗帘打开
    loc_one_curtain_suspended = '//android.view.View/android.view.View[2]/android.view.View[4]/android.view.View[2]'  # 一路窗帘暂停
    loc_one_curtain_off = '//android.view.View/android.view.View[2]/android.view.View[4]/android.view.View[3]'  # 一路窗帘关闭
    loc_more = '//android.view.View/android.view.View[1]/android.view.View/android.view.View[3]/android.view.View'  #更多

    def click_more(self):
        '''点击更多'''
        self.get_element_resourceId(self.loc_app).find_element_by_xpath(self.loc_more).click()

    def click_double_curtain_on(self):
        '''点击打开二路窗帘'''
        self.get_element_resourceId(self.loc_app).find_element_by_xpath(self.loc_double_curtain_on).click()

    def click_double_curtain_suspended(self):
        '''点击暂停二路窗帘'''
        self.get_element_resourceId(self.loc_app).find_element_by_xpath(self.loc_double_curtain_suspended).click()

    def click_double_curtain_off(self):
        '''点击关闭二路窗帘'''
        self.get_element_resourceId(self.loc_app).find_element_by_xpath(self.loc_double_curtain_off).click()

    def switch_curtain(self, name):
        '''切换窗帘'''
        self.get_element_text(name).click()