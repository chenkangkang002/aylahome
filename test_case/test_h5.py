#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：aylahome 
@File    ：test_h5.py
@IDE     ：PyCharm 
@Author  ：陈康
@Date    ：2021/5/17 18:16 
'''
from time import sleep

import allure
import pytest

from data.testData import DEVICE_LIST_DATA
from func.utils import find_h5_device_property
from func.validation_h5 import ValidationH5
from lib.page.advanced_features import AdvancedFeatures
from lib.page.base_page import BasePage
from lib.page.h5_page import H5Page
from lib.page.room_index_page import RoomIndexPage
from setting.variament import HOME_NAME, SWITCH_DEVICE


class TestH5():

    # def setup_class(self, getDriver):
    #     driver = getDriver
    #     fip = RoomIndexPage(driver)
    #     with allure.step(f'切换家庭：{HOME_NAME}，保证这里的家庭和接口获取数据的家庭一致'):
    #         fip.switch_home(HOME_NAME)

    # @allure.story('测试设备的H5')
    @pytest.mark.parametrize("deviceData", DEVICE_LIST_DATA)
    @pytest.mark.skip
    def test_h5(self, getDriver, deviceData):
        driver = getDriver
        fip =  RoomIndexPage(driver)
        nickname = deviceData['nickname']    #'罗马电地暖'
        deviceName = deviceData['deviceName']
        device_status = deviceData['deviceStatus']
        deviceId = deviceData['deviceId']
        property = 'WindSpeed'
        isH5 = deviceData['hasH5']
        allure.dynamic.title(nickname)  #动态生成标题
        af = AdvancedFeatures(driver)
        hp = H5Page(driver)
        bp = BasePage(driver)
        bp.find_ele(nickname)    #通过该方法先滚动找到元素
        with allure.step(f'点击设备列表的具体设备{nickname}'):
            fip.get_element_text(nickname).click()
        sleep(2)
        if isH5 == 1:   #存在H5页面
            try:
                assert hp.get_h5_device_name(nickname) in nickname
                if bp.get_offline_status_h5():
                    with allure.step('切换风速之后并通过接口判断值是否匹配'):
                        bp.switch_wind_speed_or_model('M3')
                        assert find_h5_device_property(deviceId,property) == '3'
                bp.screenshot(nickname)
                with allure.step('点击<返回设备列表'):
                    hp.click_back_but(deviceName)
            except Exception:
                bp.swipe_back_index()
                assert 'H5页面成功加载？？' == '加载H5页面失败'
                #罗马紧急按钮开关，罗马电地暖,人体
        else:
            assert '高级功能' == af.get_advanced_features_text()
            bp.screenshot(nickname)
            with allure.step('点击<返回设备列表'):
                af.click_advanced_features_back()

        # a = driver.contexts
        # print('contexts:',a)
        # b = MobileCommand.SWITCH_TO_CONTEXT, {"name": "WEBVIEW_com.ayla.aylahome"}
        # # b = driver.switch_to.context('WEBVIEW_com.ayla.aylahome')
        # print('NATIVE_APP:', b)
        # print('current_context:', driver.current_context)
        # c = driver.page_source
        # print('page_source:', c)
        # #通过接口获取设备在云上的属性数据
        # device_info = find_specified_device_info(home_name, device_name)
        # deviceId = device_info['deviceId']
        # url = TEST_HOST + PROPERTIES_URL.format(deviceId)
        # headers = "headers"
        # data = ""
        # ret = requests.get(url = url, headers = headers, json = data, verify = False)
        # data_json = ret.json()
        #
        #
        # hp = H5Page(driver)
        # device_name_h5 = hp.get_h5_device_name()
        # print('device_name_h5', device_name_h5)
        # assert device_name == device_name_h5

    @allure.story("遍历验证设备的H5单控")
    @pytest.mark.parametrize("deviceData", DEVICE_LIST_DATA)
    def test_002(self, getDriver, deviceData):
        driver = getDriver
        fip = RoomIndexPage(driver)
        with allure.step(f'切换家庭：{HOME_NAME}，保证这里的家庭和接口获取数据的家庭一致'):
            fip.switch_home(HOME_NAME)
        nickname = deviceData['nickname']  # '罗马电地暖'
        deviceName = deviceData['deviceName']
        device_status = deviceData['deviceStatus']  #ONLINE OFFLINE
        deviceId = deviceData['deviceId']
        isH5 = deviceData['hasH5']
        rip = RoomIndexPage(driver)
        bp = BasePage(driver)
        bp.find_ele(nickname)  # 通过该方法先滚动找到元素
        status = bp.get_offline_status_devicelist(nickname)
        #这里可以加一个控制：只点击验证在线设备，离线设备或者都验证
        # if SWITCH_DEVICE != [] and status == SWITCH_DEVICE:
        #     fip.get_element_text(deviceName).click()
        if isH5 == 1:  # 存在H5页面
            fip.get_element_text(nickname).click()
            sleep(1)
            allure.dynamic.title(deviceName)  # 动态生成标题
            # device_type
            if status == '在线':
                vh = ValidationH5(driver)
                vh.switch_validation_function(**deviceData)

            else:
                pass
        # bp.screenshot(nickname)
        # hp = H5Page(driver)
        # with allure.step('点击<返回设备列表'):
        #     hp.click_back_but(deviceName)
        # sleep(2)
        # bp = BasePage(driver)
        # bp.switch_on_off('K1')
        sleep(3)
