#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/27 23:50
# @Author  : Geda
import time
import sys
from bs4 import BeautifulSoup
import requests
import pytesseract
from PIL import Image
reload(sys)
sys.setdefaultencoding("utf-8")

from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def get_captcha():
    list=[]
    list3 = raw_input('please input code :')

    for i in (list3):
        list.append(int(i)*23)
        list.append(24)
    return [list[i:i+2]for i in range(0,len(list),2)]
class zhihu(object):
    def __init__(self,phone_num,password):
        self.phone_num=phone_num
        self.password=password
        sess = requests.session()
        self.sess=sess
    def login(self):
        #获取_xsrf 防域攻击
        login_url = 'https://www.zhihu.com/#signin'

        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        }
        html = self.sess.get(login_url,headers=headers,verify=False).text
        bs =BeautifulSoup(html,'lxml')
        _xsrf=bs.find("input",attrs={"name":"_xsrf"}).get("value")
        #生成验证码url
        nowtime = time.time() * 1000
        code_url = 'https://www.zhihu.com/captcha.gif?r=%d&type=login&lang=cn' % nowtime
        pic=self.sess.get(code_url,headers=headers).content
        with open('code.jpg','wb') as f:
            f.write(pic)
        #获取验证码对应list
        list=get_captcha()
        print list
        data = {
            '_xsrf': _xsrf,
            'captcha_type': 'cn',
            'password': self.password,
            'phone_num': self.phone_num,
            # 'password': '15235153137',
            # 'phone_num': 'g.488666',
            'captcha':'{"img_size":[200,44],"input_points":%s}'%(list)
        }
        post_url ='https://www.zhihu.com/login/phone_num'

        html=self.sess.post(post_url,data=data,headers=headers).json()
        html=html['msg']
        #查看是否登录成功
        print html
        # 查看个人主页
        resoponse = self.sess.get("https://www.zhihu.com/people/ghj-35-2/activities",headers=headers).content
        return resoponse
    def detail(self):

        print self.login()
if __name__ == '__main__':
    phone_num=raw_input('please input your phone_num:')
    password=raw_input('please input your password:')
    spider_zhihu =zhihu(phone_num,password)
    spider_zhihu.detail()