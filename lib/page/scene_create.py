#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：testgrouppub 
@File    ：scene_create.py
@IDE     ：PyCharm 
@Author  ：陈康
@Date    ：2021/5/6 17:17 
'''
from selenium.webdriver.common.by import By

from func.utils import judge_data_to_deviceLinkage
from lib.page.base_page import BasePage


class SceneCreate(BasePage):

    #定位符
    loc_a_key_perform = (By.ID, 'com.ayla.aylahome:id/rl_A_key_perform')    #一键执行
    loc_device_state_change = (By.ID, 'com.ayla.aylahome:id/rl_cloud_linkage')  #设备状态变化
    loc_local_linkage = '本地联动'
    loc_cloud_linkage = '云端联动'
    loc_cancel = (By.ID, 'com.ayla.aylahome:id/dialog_tv_cancel') #取消选择
    loc_control_device = (By.ID, 'com.ayla.aylahome:id/rl_control_device')  # 控制设备
    loc_delay_linkage = (By.ID, 'com.ayla.aylahome:id/rl_delay_link_time')  # 延迟联动
    #一键执行
    loc_add_task = (By.ID, 'com.ayla.aylahome:id/iv_task')  #新增任务（动作）入口
    loc_name1 = (By.ID, 'com.ayla.aylahome:id/ui_rl_nickname')   #命名入口
    loc_name2 = (By.ID, 'com.ayla.aylahome:id/mn_et_name')      #名称输入框
    loc_save_name = (By.ID, 'com.ayla.aylahome:id/mn_btn_save')     #保存名称按钮
    loc_replace_photo = (By.ID, 'com.ayla.aylahome:id/ui_rl_photoname')  #更换一键执行图片
    loc_delete_task = (By.ID, 'com.ayla.aylahome:id/fl_delete')     #删除任务（动作）
    loc_save_scene = (By.ID, 'com.ayla.aylahome:id/ui_btn_save')  #保存场景按钮
    '''设备联动'''
    loc_add_conditions = (By.ID, 'com.ayla.aylahome:id/iv_coodition')   #新增条件入口
    loc_effect_time = (By.ID, 'com.ayla.aylahome:id/ui_rl_time')   #生效时间
    loc_delete_condition = (By.ID, 'com.ayla.aylahome:id/fl_delete_1')  #删除条件
    loc_join_type = (By.ID, 'com.ayla.aylahome:id/tv_join_type')    #选择触发类型
    loc_meet_any = '当满足任意条件时'
    loc_meet_all = '当满足所有条件时'
    loc_cancel_type = '取消'  #取消选择
    #设置联动中大于，小于，等于的事件
    loc_greater = '大于'
    loc_less    = '小于'
    loc_equal   = '等于'

    '''元素操作'''
    def click_a_key_perform(self):
        '''点击一键执行'''
        self.get_element(self.loc_a_key_perform).click()

    def click_device_state_change(self):
        '''点击设备状态变化'''
        self.get_element(self.loc_device_state_change).click()

    def click_local_linkage(self):
        '''点击本地联动'''
        self.get_element_text(self.loc_local_linkage, 2).click()

    def click_cloud_linkage(self):
        '''点击云端联动'''
        self.get_element_text(self.loc_cloud_linkage, 2).click()

    def click_cancel(self):
        '''点击取消'''
        self.get_element(self.loc_cancel).click()

    def click_control_device(self):
        '''点击控制设备'''
        self.get_element(self.loc_control_device).click()

    def click_delay_linkage(self):
        '''点击延迟联动'''
        self.get_element(self.loc_delay_linkage).click()

    def click_add_task(self):
        '''点击新增动作/任务'''
        self.get_element(self.loc_add_task).click()

    def click_name1(self):
        '''点击命名入口'''
        self.get_element(self.loc_name1).click()

    def input_nickname(self, name):
        '''输入联动名称'''
        self.get_element(self.loc_name2).send_keys(name)

    def click_save_name(self):
        '''点击保存联动名称'''
        self.get_element(self.loc_save_name).click()

    def click_save_scene(self):
        '''点击保存场景'''
        self.get_element(self.loc_save_scene).click()

    def click_delete_task(self):
        '''点击删除动作/任务'''
        self.get_element(self.loc_delete_task).click()

    def click_add_conditions(self):
        '''点击新增条件入口'''
        self.get_element(self.loc_add_conditions).click()

    def click_delete_condition(self):
        '''点击删除条件'''
        self.get_element(self.loc_delete_condition).click()

    '''创建一键执行'''
    def create_a_key_perform(self, scene_info,scene_name):
        '''
        创建一键执行,该方法，不包含在智能页面点击创建联动入口的动作
        :param scene_info: 联动信息，字典类型，包含条件和动作，format：{'conditions':[],'actions':[['罗马四键开关','开关一','打开'],['','','']]}
        :param scene_name: 智能场景名称
        :return:
        '''
        self.click_a_key_perform()
        actions = scene_info['actions']
        count = 0
        for action in actions:
            if count > 0:
                self.click_add_task()
            count = 1
            self.click_control_device() #点击控制设备
            for v in action:    #添加动作
                self.get_element_text(v).click()
        self.click_name1()
        self.input_nickname(scene_name)
        self.click_save_name()
        self.click_save_scene()

    '''创建设备联动'''
    def create_device_linkage(self, scene_info, scene_name, type=0):
        '''创建设备联动:云端和本地，type：0表示云端，type：1表示本地'''
        judge_data_to_deviceLinkage(scene_info)
        conditions = scene_info['conditions']
        actions = scene_info['actions']
        self.click_device_state_change()
        if type == 0:   #云端联动
            self.click_cloud_linkage()
        elif type == 1:  # 本地联动
            self.click_local_linkage()
        #开始创建联动
        for condition1 in conditions[0]:
            self.get_element_text(condition1).click()
        self.click_control_device()  # 点击控制设备
        for action1 in actions[0]:
            self.get_element_text(action1).click()
        for condition in conditions[1:]:    #添加后续条件
            self.click_add_conditions()
            self.click_control_device()  # 点击控制设备
            for var in condition:
                self.get_element_text(var).click()
        for actions in actions[1:]: #添加后续动作
            self.click_add_conditions()
            self.click_control_device()  # 点击控制设备
            for var in actions:
                self.get_element_text(var).click()
        self.click_name1()
        self.input_nickname(scene_name)
        self.click_save_name()
        self.click_save_scene()



