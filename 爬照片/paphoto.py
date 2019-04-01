#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/15 12:58
# @Author  : Geda
import urllib
import urllib2
from  json import loads
import  re
from bs4 import BeautifulSoup
x=1
def geturllist():
    html = urllib2.urlopen('https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8').read()
    html = html.decode('gbk').encode('utf-8')

    return loads(html)['data']['searchDOList']

def getalbumlist(userid):
    html = urllib2.urlopen('https://mm.taobao.com/self/album/open_album_list.htm?_charset=utf-8&user_id%20={}'.format(userid)).read()
    html = html.decode('gbk').encode('utf-8')
    reg = r'<a class="mm-first" href="(.*?)" target="_blank">'
    urllist = re.findall(reg,html)
    return urllist
def getphoto (userid,albumid):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'}
    req = urllib2.Request('https://mm.taobao.com/album/json/get_album_photo_list.htm?user_id={}&{}&top_pic_id=0&cover=%2F%2Fimg.alicdn.com%2Fimgextra%2Fi1%2F176817195%2FTB1jFcMKFXXXXblXFXXXXXXXXXX_!!0-tstar.jpg&page=1&_ksTS=1502789423171_154&callback=jsonp155'.format(userid,albumid),headers=headers)
    page = urllib2.urlopen(req,timeout=20).read()
    reg = r'"picUrl":"//(.*?)"'
    s = re.findall(reg,page)
    #print s
    for b in s :
        print b
        link = "http://%s"%b

        global  x
        urllib.urlretrieve(link,'image\%s.jpg'%x)
        x += 1
        print "loading di %s  zhang "%s

for i in geturllist():
    userid =  i['userId']

    urllist = getalbumlist(userid)
    for url in urllist[::2]:

        start_index  = url.find('album_id=')

        end_index =url.find('&',start_index)
        albumid = url[start_index:end_index]

        getphoto(userid ,albumid)
        break
    break
