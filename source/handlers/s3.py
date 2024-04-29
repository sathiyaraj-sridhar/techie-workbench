"""
This is the HTTP request handler for Amazon S3.
"""

# Import custom modules.
from models.s3 import S3Object
from handlers.main import MainHandler


class S3Handler(MainHandler):
    """S3 HTTP request handler."""

    def get(self):
        """Handling HTTP GET method."""
        self.vars['s3'] = {
            'bucketname': S3Object.bucketname
        }
        self.render('s3.html',**self.vars)

    def post(self):
        """Handling HTTP POST method."""
        if self.request.path=='/s3/settings':
            S3Object.bucketname = self.get_argument('bucketname')
            self.redirect('/s3')
            return
        if self.request.path=='/s3/upload':
            pass
        self.redirect('/s3')
