# coding=utf-8
"""
@version: 2018/3/4 004
@author: Suen
@contact: sunzh95@hotmail.com
@file: hello.py
@time: 0:15
@note:  ??
"""
from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop

import tornado.web
import tornado.httpclient
import tornado.escape


class MainHandler(RequestHandler):
    @tornado.web.gen.coroutine
    def get(self):
        http = tornado.httpclient.AsyncHTTPClient()
        resp = yield http.fetch("https://dev.legendpoker.cn/weapp-redpacket/api/user/capital")
        print(resp)
        self.write(tornado.escape.json_decode(resp.body))


class StoryHandler(RequestHandler):
    def get(self, *args, **kwargs):
        index = args[0]
        if not index:
            self.write('this is the story main page')
        else:
            self.write('This is the story page: {}'.format(index))


class PostHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('<html><body><form action="/message/" method="post">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    def post(self, *args, **kwargs):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_argument("message"))


app = Application([
    (r'/', MainHandler),
    (r'/story/(.*)', StoryHandler),
    (r'/message/', PostHandler),
], autoreload=True)

if __name__ == '__main__':
    app.listen(8888)
    IOLoop.instance().start()
