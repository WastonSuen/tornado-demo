# coding=utf-8
"""
@version: 2018/3/4 004
@author: Suen
@contact: sunzh95@hotmail.com
@file: hello.py
@time: 0:15
@note:  ??
"""
from typing import Iterable

from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop


class MainHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write('Hello Tornado')


class StoryHandler(RequestHandler):
    def get(self, *args, **kwargs):
        index = args[0]
        if not index:
            self.write('this is the story main page')
        else:
            self.write('This is the story page: {}'.format(index))


app = Application([
    (r'/', MainHandler),
    (r'/story/([a-zA-Z0-9]*)', StoryHandler)
])

if __name__ == '__main__':
    app.listen(8888)
    IOLoop.instance().start()
