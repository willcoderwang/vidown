import tornado.httpserver
import tornado.ioloop
import tornado.web
import subprocess

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("I am working great")

    def put(self):
        video_url = self.request.body
        get_list = subprocess.run(["you-get", "--json", video_url], stdout=subprocess.PIPE)
        if get_list.returncode != 0:
            self.write("something went wrong, cannot get video list")
        else:
            self.write(get_list.stdout)

if __name__ == "__main__":
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(80)
    tornado.ioloop.IOLoop.instance().start()
