#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/16 17:52
# @Author  : Geda
import requests
import re
import urllib
import  os
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def get_response(url):
    response = requests.get(url).text
    return response

def get_content(html):
    reg = re.compile(r'(<div class="j-r-list-c">.*?</div>.*?</div>)',re.S)
    return  re.findall(reg,html)

def get_mp4_url(content):
    reg = r'data-mp4="(.*?)"'
    return re.findall(reg,content)

def get_mp4_name (response):
    reg = re.compile(r'<a href="/detail-.{8}.html">(.*?)</a>')
    return  re.findall(reg,response)

def downmp4(mp4_url,path):
    path = ''.join(path.split())
    path = 'E:\\xx\\{}.mp4'.format(path.decode('utf-8').encode('gbk'))
    if not os.path.exists(path):

        urllib.urlretrieve(mp4_url,path)
        print 'ok!'
    else:
        print 'no!'

def get_url_name(start_url):
    content = get_content(get_response(start_url))
    for i  in content:
        mp4_url = get_mp4_url(i)

        if mp4_url:
            mp4_name = get_mp4_name(i)
            #print mp4_url[0], mp4_name[0]
            downmp4(mp4_url[0],mp4_name[0])



if __name__ == '__main__':
    start_url ='http://www.budejie.com/'
    get_url_name(start_url)






