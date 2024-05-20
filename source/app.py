"""
Techie Workbench
Tailor-Made for Exploring AWS
"""

# Import standard modules.
import os

# Import community modules.
import tornado

# Import custom modules.
from config import appconf,sysconf
from logger import logger
from models.redis import Redis
from handlers.main import MainHandler
from handlers.settings import SettingsHandler
from handlers.s3 import S3Handler

# Port on which the Tornado listens, this can be passed as command line arguments.
tornado.options.define('port',default=80,type=int)


class App(tornado.web.Application):
    """Tornado App initializer."""

    def __init__(self):

        self.conf = appconf
        self.sysconf = sysconf
        self.redis = Redis

        settings = {
          "template_path":os.path.join(os.path.dirname(__file__),'templates'),
          "cookie_secret":self.conf['cookie_secrent'],
          "xsrf_cookies":True,
          "debug":True,
          "serve_traceback":False,
          "compress_response":True,
          "autoreload":True,
          "template_whitespace":"all",
          "static_path":os.path.join(os.path.dirname(__file__),'static'),
          "static_url_prefix":self.conf['static_url_prefix']
        }

        handlers = [
          (r'/',MainHandler),
          (r'/health',MainHandler),
          (r'/home',MainHandler),
          (r'/settings',SettingsHandler),
          (r'/s3',S3Handler),
          (r'/s3/settings',S3Handler),
          (r'/s3/upload',S3Handler),
          (r'/s3/delete',S3Handler)
        ]

        tornado.web.Application.__init__(self,handlers,**settings)

if __name__=='__main__':
    tornado.options.parse_command_line()
    HttpServer = tornado.httpserver.HTTPServer(App(),xheaders=True)
    try:
        HttpServer.listen(tornado.options.options.port)
        logger.info('Starting App...')
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        logger.info('Stopping App...')
    finally:
        tornado.ioloop.IOLoop.instance().stop()
