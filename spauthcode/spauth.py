#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/18 14:01
# @Author  : Geda


from tornado import web
from tornado import httpserver
from tornado import ioloop
import check_code
import cStringIO

class Indexhandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('hello world!')

class LoginHadler(web.RequestHandler):
    def get(self, *args, **kwargs):
        #self.write('登录模块')
        self.render('authcode.html')

    def post(self,*args,**kwargs):
        username= self.get_argument('username')
        password= self.get_argument('password')
        if username == 'admin' and password == '123456':
            self.write('登录成功')
        else:
            self.write('用户密码错误')
class ImgHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        with open('233.jpg','rb')as f:
            img_data = f.read()
            self.write(img_data)
            self.set_header("Content-Type","image/jpeg")

class CheckCodeHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        img, code= check_code.create_validate_code()
        #mstream = cStringIO.BytesIO()
        #img.save(mstream, 'GIF')
        img.show()
        print(code)
        #self.write(mstream.getvalue())


application = web.Application([
            (r"/index", Indexhandler),
            (r"/login", LoginHadler),
            (r"/img", ImgHandler),
            (r"/check_code", CheckCodeHandler),

        ])

if __name__ == '__main__':
        http_server = httpserver.HTTPServer(application)
        http_server.listen(8180)
        ioloop.IOLoop.current().start()