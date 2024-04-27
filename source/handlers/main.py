"""
This is the main HTTP request handler.
"""

# Import community modules.
from tornado.web import HTTPError

# Import community modules.
import tornado


class MainHandler(tornado.web.RequestHandler):
    """Main HTTP request handler."""

    def initialize(self):
        """Called before handling HTTP methods."""
        self.application.notify = None

    def get(self):
        """Handling HTTP GET method."""
        if self.request.path=='/':
            self.redirect('/home')
            return
        if self.request.path=='/health':
            self.write('ok')
            return
        if self.request.path=='/home':
            self.render('home.html',sysconf=self.application.sysconf,notify=self.application.notify)
            return
        raise HTTPError(400)
