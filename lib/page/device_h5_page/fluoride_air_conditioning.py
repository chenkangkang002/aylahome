#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：aylahome 
@File    ：fluoride_air_conditioning.py  #氟空调
@IDE     ：PyCharm 
@Author  ：陈康
@Date    ：2021/6/7 14:47 
'''
from time import sleep

from lib.page.base_page import BasePage


class FluorideAirConditioning(BasePage):

    loc_online_status = '//android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[12]/android.view.View[1]/android.view.View[2]' #在离线状态
    loc_set_temperature = '//android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[12]/android.view.View[2]/android.view.View[2]/android.view.View[1]'    #设置温度
    loc_current_temperature = '//android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[12]/android.view.View[3]'   #当前温度
    loc_cool = '//android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[12]/android.view.View[2]/android.view.View[1]/android.view.View'  #降温
    loc_heat_up = '//android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[12]/android.view.View[2]/android.view.View[3]/android.view.View'   #升温
    loc_on_off_butt = '//android.view.View/android.view.View[2]/android.view.View[6]/android.view.View[3]/android.widget.Image'   #开关按钮

    def get_online_status(self):
        '''获取设备在离线状态'''
        return self.get_children_element_to_parent(self.loc_online_status).text

    def get_set_temperature(self):
        '''获取设置的温度'''

    def click_control_temperature(self,number,type:int):
        '''
        点击控制温度
        :param number: 降低的度数
        :param type: 控制温度的类型,0为降温，1为升温
        :return:
        '''
        if isinstance(number,int) or isinstance(number,str):
            for var in range(int(number)):
                if int(type) == 0:
                    self.get_element(self.loc_cool).click()
                elif int(type) == 1:
                    self.get_element(self.loc_heat_up).click()
                else:
                    return '控制类型错误'
                sleep(1)
        else:
            return '输入正确的温度'