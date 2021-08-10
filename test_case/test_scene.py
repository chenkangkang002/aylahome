#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：testgrouppub 
@File    ：test_scene.py
@IDE     ：PyCharm 
@Author  ：陈康
@Date    ：2021/4/29 19:43 
'''
import os
import sys

# curPath = os.path.abspath(os.path.dirname(__file__))
# print(curPath)
# rootPath = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# print(rootPath)
# sys.path.append(rootPath)
# print(sys.path)
# sys.path.append("..")
import allure
import pytest

from lib.page.room_index_page import RoomIndexPage
from lib.page.scene_create import SceneCreate
from lib.page.scene_index_page import SceneIndexPage

@allure.story('验证智能场景创建')
class TestScene():

    @allure.story('创建一键执行')
    def test_create_a_key_perform(self,getDriver):
        driver = getDriver
        fip = RoomIndexPage(driver)
        fip.click_scene()
        sip = SceneIndexPage(driver)
        sip.click_intelligence_add()
        sc = SceneCreate(driver)
        scene_info = {'conditions': [], 'actions': [['米兰三路智能面板', '筒灯', '开启']]}
        scene_name = '测试吧'
        sc.create_a_key_perform(scene_info, scene_name)
        sip.click__a_key_perform_tag()
        scene_list = sip.get_scene_list_text(sip.loc_devices_link_table)
        print(scene_list)
        assert scene_name in scene_list

    @allure.story('创建云端联动')
    def test_create_cloud_linkage(self):
        pass

    @allure.story('创建本地联动')
    def test_create_local_linkage(self):
        pass



