import tornado.web
import tornado.ioloop
from tornado.options import define, options

define("host", default='127.0.0.1', help="run on the given host")
define("port", default=8866, help="run on the given port", type=int)
define("debug", default=False, help="run in debug mode")


class BlogDetail(tornado.web.RequestHandler):
    def set_default_headers(self) -> None:
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', 'x-requested-with')
        self.set_header('Access-Control-Allow-Methods', 'GET')

    def get(self):
        filePath = self.get_argument('filePath')
        if not filePath:
            raise tornado.web.HTTPError(404)
        with open(filePath, 'rb') as f:
            self.set_header("Content-Type", "application/json; charset=UTF-8")
            self.write(f.read())


class BlogSettings(tornado.web.RequestHandler):
    def set_default_headers(self) -> None:
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', 'x-requested-with')
        self.set_header('Access-Control-Allow-Methods', 'GET')

    def get(self):
        with open('./settings.json', 'rb') as f:
            self.set_header("Content-Type", "application/json; charset=UTF-8")
            self.write(f.read())


def run_app():
    app = tornado.web.Application([
        ('/api/blog', BlogDetail),
        ('/api/settings', BlogSettings)
    ])
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    run_app()
