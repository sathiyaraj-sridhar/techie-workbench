"""
This is the HTTP request handler for Amazon S3.
"""

# Import standard modules.
import io

# Import custom modules.
from models.s3 import S3Object
from handlers.main import MainHandler


class S3Handler(MainHandler):
    """S3 HTTP request handler."""

    def get(self):
        """Handling HTTP GET method."""
        self.vars['s3'] = {}
        self.vars['s3']['bucketname'] = S3Object.bucketname
        self.vars['s3']['connection'] = S3Object.conn
        if S3Object.conn['status']=='success':
            self.vars['s3']['objects'] = S3Object.list()
        else:
            self.vars['s3']['objects'] = []
        self.render('s3.html',**self.vars)

    def post(self):
        """Handling HTTP POST method."""
        if self.request.path=='/s3/settings':
            S3Object.bucketname = self.get_argument('bucketname')
            S3Object.reconnect()
            self.redirect('/s3')
            return
        if self.request.path=='/s3/upload':
            key = self.get_argument('key')
            data = io.BytesIO(self.request.files['object'][0]['body'])
            S3Object.upload(data,key)
        if self.request.path=='/s3/delete':
            key = self.get_argument('key')
            S3Object.delete(key)
        self.redirect('/s3')
