#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/19 19:16
# @Author  : Geda

import  requests
import  re
import random
def readkami():
    kami=[]
    with open('C:/Users/GUO/Desktop/baiwanmima.txt') as f:
        for line in f.readlines():

            kami.append(line)

    return kami
def login(kami,yaoqingma):
    sess =requests.session()
    url ='http://www.wonter.net/submit/'
    headers={
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36'
    }

    data=sess.get(url=url,headers=headers).content
    #print data
    reg="<input type='hidden' name='csrfmiddlewaretoken' value='(.*?)' />"
    csrfmiddlewaretoken=re.findall(reg,data)

    data = {
        'csrfmiddlewaretoken': csrfmiddlewaretoken[0],
        'ticket': kami,
        'invite_code': yaoqingma
    }

    result =sess.post(url,headers=headers,data=data).content
    reg2="<p class=.*>(.*?)</p>"
    result=re.findall(reg2,result,re.S)
    return result[0]
if __name__ == '__main__':
    #print  login(readkami()[1])
    yaoqingma =['fvsnp','d9z42','fura8','V27BN']
    for kami  in readkami():
        x=random.randint(0, 3)
        yaoqingma1 =yaoqingma[x]
        print yaoqingma1,kami
        #print login(kami,yaoqingma1)
