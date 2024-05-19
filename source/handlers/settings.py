"""
This is the settings HTTP request handler.
"""

# Import custom modules.
from handlers.main import MainHandler


class SettingsHandler(MainHandler):
    """S3 HTTP request handler."""

    def get(self):
        """Handling HTTP GET method."""
        self.vars['redis'] = {
            'host': self.application.redis.host,
            'port': self.application.redis.port,
            'connection': self.application.redis.status()
        }
        self.render('settings.html',**self.vars)

    def post(self):
        """Handling HTTP POST method."""
        host = self.get_argument('host')
        port = self.get_argument('port')
        self.application.redis.reconnect(host,port)
        self.redirect('/settings')
