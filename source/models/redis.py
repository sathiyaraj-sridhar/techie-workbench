"""
Redis model
"""

# Import community modules.
import redis

# Import custom modules.
from config import appconf


class Redis:
    """Manage Redis database."""
    def __init__(self):
        """Initializer. """
        self.host = appconf['redis']['host']
        self.port = appconf['redis']['port']
        self.conn = self.connect()

    def connect(self):
        """Instantiate a Redis connection."""
        return redis.Redis(host=self.host,port=self.port,decode_responses=True,socket_timeout=0.01)

    def reconnect(self,host=None,port=None):
        """Instantiate a Redis connection, specifying a different host and port."""
        if host is not None and port is not None:
            self.host = host
            self.port = port
            self.conn = self.connect()

    def status(self):
        """Returns the status of the Redis connection."""
        try:
            self.conn.ping()
            return {'status':'success','message':'Connection successful.'}
        except redis.exceptions.ConnectionError as error:
            return {'status':'failure','message':str(error)}
        except redis.exceptions.TimeoutError as error:
            return {'status':'failure','message':str(error)}

    def set(self):
        """Set the data."""

    def get(self):
        """Get the data."""


Redis = Redis()
