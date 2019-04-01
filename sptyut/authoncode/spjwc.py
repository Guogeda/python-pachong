#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/27 17:12
# @Author  : Geda
import  requests
import  sys
import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

reload(sys)
sys.setdefaultencoding("utf-8")

def login():
    driver = webdriver.PhantomJS(executable_path=r'E:\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    driver.get('http://202.207.247.44:8089/')
    driver.save_screenshot('jiaowuchu.png')
    code=raw_input('code:')
    driver.find_element_by_name("zjh").send_keys('2015006602')
    driver.find_element_by_name("mm").send_keys('190099')
    driver.find_element_by_name("v_yzm").send_keys(code)
    driver.find_element_by_xpath('//*[@id="btnSure"]').click()

    driver.get('http://202.207.247.44:8089/jxpgXsAction.do?oper=listWj')
    #driver.find_element_by_partial_link_text("教学评估").click()

    driver.save_screenshot('jiemian.png')







login()