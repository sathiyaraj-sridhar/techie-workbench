"""
S3 model
"""

# Import custom modules.
from config import appconf


class S3Object:
    """Manage S3 database."""
    def __init__(self):
        """Initializer. """
        self.bucketname = appconf['s3']['bucketname']

    def list(self):
        """Read the objects."""

    def upload(self):
        """Upload the object."""


S3Object = S3Object()
