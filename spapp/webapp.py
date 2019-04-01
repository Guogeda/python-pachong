#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/18 20:24
# @Author  : Geda

from flask import Flask
from flask import  render_template
from flask import  request
app = Flask(__name__)

@app.route('/369')
def index():
    return render_template('index.html',name = u'疙瘩')

@app.route('/upload',methods =['GET','POST'] )#默认的请求方式get
def upload():
    file = request.files.get('file')
    if not file:
        return u'请先选择文件上传'
    file.save('static/%s.txt'%file.filename)
    return u'谢谢'

if __name__ == '__main__':
    app.run(debug=True)