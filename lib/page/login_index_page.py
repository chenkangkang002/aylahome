'''登录页'''
from selenium.webdriver.common.by import By
from lib.page.base_page import BasePage
from lib.page.room_index_page import FjIndexPage


class LoginIndexPage(BasePage):

    #定位符
    loc_input_board = (By.ID, 'com.ayla.aylahome:id/edit_account')  #账号输入框
    loc_login_type = (By.ID, 'com.ayla.aylahome:id/login_tv_toggle')  #登录方式切换
    loc_login_submit = (By.ID, 'com.ayla.aylahome:id/mLoginBtn')   #登录提交按钮
    loc_login_agreement = (By.ID, 'com.ayla.aylahome:id/login_cb_agreement')    #协议
    loc_verify_code = (By.ID, 'com.ayla.aylahome:id/verificationCodeEditText')    #验证码
    loc_input_password = (By.ID, 'com.ayla.aylahome:id/pi_et_password')  #密码输入框
    loc_forget_password = (By.ID, 'com.ayla.aylahome:id/pi_tv_forget')  #忘记密码按钮

    #元素操作
    def input_username(self, username):
        '''输入用户名'''
        ele = self.get_element(self.loc_input_board)
        ele.clear()
        ele.send_keys(username)

    def input_password(self, password):
        '''输入密码'''
        ele = self.get_element(self.loc_input_password)
        ele.clear()
        ele.send_keys(password)

    def click_login_type(self):
        '''点击切换登录方式'''
        self.get_element(self.loc_login_type).click()

    def click_login_submit(self):
        '''提交登录信息：点击登录按钮'''
        self.get_element(self.loc_login_submit).click()

    def click_login_agreement(self):
        '''点击同意用户协议'''
        self.get_element(self.loc_login_agreement).click()

    def input_verify_code(self, verify_code):
        '''输入验证码'''
        ele = self.get_element(self.loc_verify_code)
        ele.clear()
        ele.send_keys(verify_code)

    #页面功能
    def choose_login_type(self, type = 1):
        '''
        切换登录类型（账号密码/验证码）
        :param type: 0/1:0是验证码登录，1是账号密码登录
        :return:
        '''
        login_type_text = self.get_assert(self.loc_login_type)
        if type == 0 and login_type_text == '验证码登录':
            '''验证码登录'''
            self.click_login_type()
        elif type == 1 and login_type_text == '密码登录':
            '''密码登录'''
            self.click_login_type()
        else:
            return False    #输入错误的数据类型
        return True

    def login(self, username, password, type=1,verify_code=123456):
        '''登录'''
        self.input_username(username)
        if not self.choose_login_type(type):
            return '请输入正确的登录类型（0/1）'
        self.click_login_submit()
        if type:
            '''密码'''
            self.input_password(password)
            self.click_login_submit()
        else:
            '''验证码'''
            self.input_verify_code(verify_code)

        fj = FjIndexPage(self.driver)
        return self.get_assert(fj.loc_my_home)