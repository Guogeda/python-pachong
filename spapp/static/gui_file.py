#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/18 21:48
# @Author  : Geda
from Tkinter import *
from tkFileDialog import *
import  urllib2

def upload():
    filename = askopenfilename(title = '选择文件')
    file = open(filename,'rb').read()
    url = 'http://127.0.0.1:5000/'

root = Tk()
root.title('文件分享软件')
root.geometry('300*140+900+300')
ent=Entry(root,width=40).grid()
ent.grid()
btn_up = Button (root,text= '  上  传 ',command=upload())
btn_up.grid()
btn_wn = Button (root,text='   下  载',command=)
btn_wn.grid()
mainloop()#显示窗口