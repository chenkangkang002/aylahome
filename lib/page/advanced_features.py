#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：aylahome 
@File    ：advanced_features.py
@IDE     ：PyCharm 
@Author  ：陈康
@Date    ：2021/5/26 17:26 
'''
from selenium.webdriver.common.by import By

from lib.page.base_page import BasePage


class AdvancedFeatures(BasePage):

    loc_advanced_features_text = (By.ID, 'com.ayla.aylahome:id/mTitleTv')   #定位高级功能页面文案
    loc_back_003 = (By.ID, 'com.ayla.aylahome:id/mLeftIv') #高级功能页面返回按钮

    def get_advanced_features_text(self):
        '''获取高级页面的文案'''
        return self.get_assert(self.loc_advanced_features_text)

    def click_advanced_features_back(self):
        '''点击高级功能页面的返回按钮'''
        self.get_element(self.loc_back_003).click()