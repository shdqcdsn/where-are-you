import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, yijiao")

application = tornado.web.Application([
    (r"/", MainHandler),
])

