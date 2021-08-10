'''智能首页'''
from selenium.webdriver.common.by import By

from lib.page.base_page import BasePage


class SceneIndexPage(BasePage):

    #定位符
    loc_intelligence_add = (By.ID , 'com.ayla.aylahome:id/iv_intelligence_add')   #添加智能
    loc_a_key_perform_tag = '一键执行'   #一键执行
    loc_devices_link_tag = '设备联动' #设备联动
    loc_one_play_class = (By.CLASS_NAME, 'android.view.ViewGroup')  #一键执行任务集合
    loc_one_play_open_but = (By.ID, 'com.ayla.aylahome:id/tv_status')  #一键执行任务启动按钮

    loc_devices_link_table = (By.CLASS_NAME, 'android.view.ViewGroup')  #设备联动列表
    loc_devices_link_class = (By.CLASS_NAME, 'android.widget.RelativeLayout')   #设备联动任务集合
    loc_device_link_name = (By.ID, 'com.ayla.aylahome:id/tv_name')  #任务名称

    loc_device_link_but = (By.ID, 'com.ayla.aylahome:id/switch_open')   #设备联动任务开关

    def click_intelligence_add(self):
        '''点击添加智能，右上角按钮'''
        self.get_element(self.loc_intelligence_add).click()

    def click__a_key_perform_tag(self):
        '''点击一键执行tag'''
        self.get_element_text(self.loc_a_key_perform_tag).click()

    def click_devices_link_tag(self):
        '''点击设备联动tag'''
        self.get_element_text(self.loc_devices_link_tag).click()



