#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：testgrouppub 
@File    ：run.py
@IDE     ：PyCharm 
@Author  ：陈康
@Date    ：2021/5/16 11:11 
'''
import os

import pytest

if __name__ == '__main__':
    pytest.main()   #["-s", "./test_case/", "--alluredir=./allure/allure_result/"]
    # command = 'allure generate allure/allure_result -o allure/allure_report --clean'
    # os.system(command)
    #生成测试报告：allure generate allure/allure_result -o allure/allure_report --clean