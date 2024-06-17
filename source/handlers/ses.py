"""
This is the HTTP request handler for Amazon SES.
"""

# Import custom modules.
from models.ses import SES
from handlers.main import MainHandler


class SESHandler(MainHandler):
    """SES HTTP request handler."""

    def get(self):
        """Handling HTTP GET method."""
        self.vars['ses'] = {}
        self.vars['ses']['source'] = SES.source
        self.vars['ses']['connection'] = SES.conn
        self.render('ses.html',**self.vars)

    def post(self):
        """Handling HTTP POST method."""
        if self.request.path=='/ses/settings':
            SES.source = self.get_argument('source')
            SES.reconnect()
            self.redirect('/ses')
            return
        if self.request.path=='/ses/sendemail':
            destination = self.get_argument('destination')
            subject = self.get_argument('subject')
            body = self.get_argument('body')
            SES.send_email(destination,subject,body)
        self.redirect('/ses')
