'''page基类'''
import glob
import random
import time

import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from setting.attribute_enum import DeviceAttribute
from setting.config import BASE_PATH
from setting.variament import TIMEOUT


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def scree_shot(self,path='../image/'):
        '''截图'''
        self.driver.save_screenshot()

    def screenshot(self, case_name):
        '''截图'''
        # 获取时间并进行格式化
        start_time = time.strftime('%Y-%m-%d %H_%M_%S')
        # 拼接文件路径
        filepath = f'{BASE_PATH}\\allure\\image\\{case_name}_{start_time}.png'
        self.driver.get_screenshot_as_file(filepath)
        allure.attach(filepath, f'{case_name}的H5页面截图',
                      attachment_type=allure.attachment_type.PNG)

    def picturereading(self, image_name):  # bookneme输入图片名字方便在图片目录中找到对应的图片
        image_path = f'{BASE_PATH}\\allure\\image\\{image_name}'
        image = glob.glob(image_path + '_*.png')
        return image

    def get_element(self, location):
        '''
        得到单个元素/控件对象
        :param location: 元素定位符(By.ID, 'id')
        :return: 单个元素对象
        '''
        return WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*location))
        # return self.driver.find_element(*location)

    def get_elements(self, location):
        '''
        得到元素对象集合
        :param location: 元素定位符(By.ID, 'id')
        :return: 元素对象集合
        '''
        return self.driver.find_elements(*location)

    def get_random_element(self, location):
        '''
        得到随机元素对象
        :param location: 元素定位符(By.ID, 'id')
        :return: 随机的元素对象
        '''
        elements = self.get_elements(*location)  #获得元素集合
        ele_len = len(elements)     #获得元素集合长度
        random_index = random.randint(0,ele_len)    #获得随机数
        return elements[random_index] #返回随机元素对象

    def get_assert(self, location):
        '''
        获取断言信息
        :param location: 元素定位符(By.ID, 'id')
        :return: 元素的文本信息
        '''
        return self.get_element(location).text

    def get_assert_to_text(self, text):
        '''
        获取断言信息,通过text定位元素是否存在
        :param text: 元素定位符(By.ID, 'id')
        :return: 元素的文本信息
        '''
        return self.driver.find_element_by_android_uiautomator('new UiSelector().text("{}")'.format(text))

    def get_index_device(self, text):
        '''
        通过文本信息定位首页设备列表的device元素对象
        :param text: 文本信息
        :return: 单个元素对象
        '''
        ret = None
        try:
            self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("{}")'.format(text))
            ret = True
        except NoSuchElementException:
            ret = False
        finally:
            return ret

    def get_element_text(self, text, type=0):
        '''
        通过文本信息定位元素对象
        :param text: 文本信息
        :param type: 查找类型：0/1/2，0：文本完全匹配，1：包含文本，2：以文本开头
        :return: 单个元素对象
        '''
        loc = None
        if type == 0:
            loc = 'new UiSelector().text("{}")'.format(text)
        elif type == 1:
            loc = 'new UiSelector().textContains("{}")'.format(text)
        elif type == 2:
            loc = 'new UiSelector().textStartsWith("{}")'.format(text)

        return WebDriverWait(self.driver, TIMEOUT).until(lambda x: x.find_element_by_android_uiautomator(loc))
        # return self.driver.find_element_by_android_uiautomator(loc)

    def get_element_resourceId(self, resource_id):
        '''
        通过resourceId信息定位元素对象
        :param resource_id: resource_id
        :return: 单个元素对象
        '''
        loc = 'new UiSelector().resourceId("{}")'.format(resource_id)
        return self.driver.find_element_by_android_uiautomator(loc)

    def get_element_bounds(self):
        '''获取单控页开关按钮的bounds信息'''
        loc_dk = (By.CLASS_NAME, 'android.widget.Image')
        print(1)
        return self.get_element(loc_dk).location

    def get_swipe(self, fx = 'l'):
        '''
        滑动，根据传入的参数控制滑动的方向
        :param fx: 滑动方向，默认向左'l'，向右r，向上u，向下d
        :return:
        '''
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        x_c = 0.5 * width
        x_l = 0.3 * width
        x_r = 0.7 * width
        y_c = 0.5 * height
        y_u = 0.4 * height
        y_d = 0.7 * height
        if fx == 'l':
            self.driver.flick(x_r, y_c, x_l, y_c)
        elif fx == 'r':
            self.driver.flick(x_l, y_c, x_r, y_c)
        elif fx == 'u':
            # self.driver.flick(x_c, y_d, x_c, y_u)
            self.driver.swipe(x_c, y_d, x_c, y_u, 500)  # 从下往上滑动
        elif fx == 'd':
            self.driver.flick(x_c, y_u, x_c, y_d)
        else:
            return '请输入正确的方向'

    def get_scroll(self, start_text, end_text):
        '''
        从一个元素滑动到另一个元素
        :param start_ele:start_ele=开始元素的文本信息
        :param end_ele:end_ele=结束元素的文本信息
        :return:
        '''
        start_ele = self.get_element_text(start_text)
        end_ele = self.get_element_text(end_text)
        self.driver.scroll(start_ele, end_ele)

    def click_open_task(self, taskName):
        '''
        点击执行某名称的一键执行任务
        :param taskName: 任务名称
        :return:
        '''
        class_name = self.get_element_text(taskName).get_attribute('class')
        #通过classname得到元素集合
        loc_class_name = (By.CLASS_NAME , class_name)
        #获取元素并点击
        self.get_element(loc_class_name)[2].click()

    def get_scene_list_text(self, loc):
        '''
        获取智能列表下每个智能场景的场景名称
        :param loc: 元素集合的定位符
        :return: 元素text的list
        '''
        elements = self.get_elements(loc)
        print(elements)
        element_texts = []
        for ele in elements:
            element_texts.append(ele.text)
        print(element_texts)
        return element_texts

    def find_ele(self,devicename):
        '''向上滑动寻找元素'''
        x = 1
        ele_action_note = None
        while x:
            if self.get_index_device(devicename):
                x = False
            else:
                self.get_swipe('u')
        return ele_action_note

    def swipe_back_index(self):
        '''
        通过滑动，从H5页面返回设备列表首页，
        用于H5页面无法加载出来的情况使用与部分机型，
        '''
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        x_start = 0
        x_end = 0.7 * width
        y_start = 0.5 * height
        # driver.flick(x_start, y_start, x_end, y_start)
        self.driver.swipe(x_start, y_start, x_end, y_start, 500)  # 从左屏幕边缘往右滑动

    def get_children_element_to_parent(self,children_path,parent_element='app'):
        '''
        通过父级元素和子元素的xpath来定位子元素
        :param parent_element: 父级元素的定位符
        :param children_path: 子元素的xpath
        :return: 子元素对象
        '''
        self.get_element_resourceId(parent_element).find_element_by_xpath(children_path)

    def switch_wind_speed_or_model(self,value,type=0):
        '''
        根据档位切换风速或者切换空调模式
        :param value: 风速档位：S1,S2,S3|空调模式：M1,M2,M3,M4
        :param type: 空调模式 0：有弹框，1：无弹框
        :return:
        '''
        value = value.upper()
        if value in DeviceAttribute.get_all_name():
            if value.startswith('M') and int(type) == 0:
                self.get_element_text('模式').click()
            self.get_element_text(DeviceAttribute[value].value).click()
        else:
            return '请输入正确的切换属性'

    def switch_on_off(self, value):
        '''
        根据value将开关置为对应的状态
        :param value: K1=on,K2=off
        :return:
        '''
        value = value.upper()
        if value in DeviceAttribute.get_all_name():
            time.sleep(1)
            if value == 'K1':
                try:
                    self.get_element_text(DeviceAttribute['K2'].value).click()
                except Exception:
                    print('这里不做处理')
            elif value == 'K2':
                try:
                    self.get_element_text(DeviceAttribute['K1'].value).click()
                except Exception:
                    print('这里不做处理')
        else:
            return '请输入正确的切换属性'

    def get_offline_status_h5(self):
        '''获取h5内的在离线状态'''
        return self.get_element_text('在线', type = 1)

    def get_offline_status_devicelist(self, deviceName):
        '''
        获取设备列表上对应设备的在离线状态
        following-sibling::节点类型    得到当前节点之后的所有节点类型的节点，通过[x]来确定要第几个元素，只有一个则可不写
        preceding-sibling::节点类型    得到当前节点之前的所有节点类型的节点，通过[x]来确定要第几个元素，只有一个则可不写
        '''
        return self.driver.find_element(By.XPATH,
                                 f'//android.widget.TextView[@text="{deviceName}"]/following-sibling::android.widget.TextView[1]').text