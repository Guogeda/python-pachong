#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/18 23:32
# @Author  : Geda

import wordcloud
import matplotlib.pyplot as plt
import numpy as np


def get_wordcloud():
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr
    import time

    my_sender = '1725128685@qq.com'  # 发件人邮箱账号
    my_pass = 'mwqmewtmfrombjgg'  # 发件人邮箱密码
    my_user = '564841614@qq.com'  # 收件人邮箱账号，我这边发送给自己

    try:
        msg = MIMEText('你是个变态', 'plain', 'utf-8')
        msg['From'] = formataddr(["Fromgeda",my_sender ])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(['', my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "你是个变态"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()
    except Exception:
        print 'defaut'
if __name__ == '__main__':
    n=10
    while n:
        get_wordcloud()

        n-=1