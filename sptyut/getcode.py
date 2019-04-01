#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/20 14:16
# @Author  : Geda

from PIL import Image
from pytesser import *



def getcode():
    img=Image.open('authoncode/image.jpg')

    img_grey = img.convert('L')


    threshold = 140
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    img_out = img_grey.point(table, '1')

    text = image_to_string(img_out)  # 将图片转成字符串
    return text[0:4]

if __name__=='__main__':
    print getcode()
    print len(getcode())

