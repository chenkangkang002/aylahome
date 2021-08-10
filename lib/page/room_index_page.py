'''房间默认首页page'''
from selenium.webdriver.common.by import By

from lib.page.base_page import BasePage


class RoomIndexPage(BasePage):

    #元素定位符
    loc_my_home = (By.ID, 'com.ayla.aylahome:id/tv_my_home')    #欢迎回家
    loc_add_devices = (By.ID, 'com.ayla.aylahome:id/iv_add_devices')    #添加设备
    loc_fj_scroll_view = (By.ID, 'com.ayla.aylahome:id/scroll_view')     #房间滑动条
    loc_homes_group = (By.CLASS_NAME, 'android.widget.TextView')    #房间元素集合
    loc_rv_device = (By.ID, 'com.ayla.aylahome:id/rv_device')  #设备列表
    loc_devices_group =  (By.CLASS_NAME, 'android.view.ViewGroup')     #设备元素集合
    loc_device_icon = (By.ID, 'com.ayla.aylahome:id/iv_icon')    #设备icon
    loc_device_name = (By.ID, 'com.ayla.aylahome:id/tv_name')    #设备名称
    loc_device_status_deng = (By.ID, 'com.ayla.aylahome:id/iv_point')    #设备转台指示灯
    loc_device_status_text = (By.ID, 'com.ayla.aylahome:id/tv_status')  #设备状态文字
    loc_home_name = (By.ID, 'com.ayla.aylahome:id/tv_home_name')    #家庭展示/切换
    loc_home_list = (By.ID, 'com.ayla.aylahome:id/rv_content')  #家庭下拉列表
    loc_select_home = (By.ID, 'com.ayla.aylahome:id/tv_name')  #家庭下拉列表数据的ID

    loc_fj = (By.ID, 'com.ayla.aylahome:id/rb_main_fragment_device')   #房间
    loc_scene = (By.ID, 'com.ayla.aylahome:id/rb_main_fragment_linkage')   #智能
    loc_my = (By.ID, 'com.ayla.aylahome:id/rb_main_fragment_test')     #我的

    def click_my_home(self):
        '''点击欢迎回家'''

    def click_add_devices(self):
        '''点击添加设备'''
        self.get_element(self.loc_add_devices).click()

    def click_device_random(self):
        '''随机点击设备'''
        self.get_random_element(self.loc_devices_group).click()

    def get_device_list(self):
        '''获取设备列表'''
        self.get_elements(self.loc_devices_group)

    def click_device_choose(self, devicesName):
        '''
        点击指定名称的设备
        :param devicesName: 设备名称
        :return:
        '''
        self.get_element_text(devicesName).click()

    def get_device_status(self):
        '''获取设备的状态'''
        return self.get_assert(self.loc_device_status_text)

    def click_fj(self):
        '''点击房间'''
        self.get_element(self.loc_fj).click()

    def click_scene(self):
        '''点击智能'''
        self.get_element(self.loc_scene).click()

    def click_my(self):
        '''点击我的'''
        self.get_element(self.loc_my).click()

    def switch_home(self, homeName):
        '''切换家庭'''
        home_ele = self.get_element(self.loc_home_name)
        if home_ele.text != homeName:
            self.get_element(self.loc_home_name).click()
            self.get_element_text(homeName).click()

    def enter_home_manager(self):
        '''进入家庭管理'''
        self.get_element(self.loc_home_name).click()
        self.get_element(self.loc_home_list).find_elements(*self.loc_select_home)[-1].click()




