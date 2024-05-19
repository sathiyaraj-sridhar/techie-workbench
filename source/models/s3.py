"""
S3 model
"""

# Import community modules.
import boto3
import botocore

# Import custom modules.
from config import appconf


class S3:
    """Manage S3 bucket objects."""
    def __init__(self):
        """Initializer. """
        self.bucketname = appconf['s3']['bucketname']
        self.conn = self.connect()

    def connect(self):
        """Instantiate S3 service connection."""
        try:
            config = botocore.config.Config(connect_timeout=2,read_timeout=2)
            self.s3 = boto3.client('s3',config=config)
            self.s3.list_objects_v2(Bucket=self.bucketname)
            return {'status':'success','message':'Connection successful.'}
        except Exception as error:
            return {'status':'failure','message':str(error)}

    def reconnect(self):
        """Re-Instantiate S3 service connection."""
        self.s3.close()
        self.conn = self.connect()

    def list(self):
        """Read the objects."""
        response = self.s3.list_objects_v2(
            Bucket=self.bucketname
        )
        if 'Contents' in response:
            return response['Contents']
        return []

    def upload(self,data,key):
        """Upload the object."""
        response = self.s3.upload_fileobj(
            Fileobj=data,
            Bucket=self.bucketname,
            Key=key,
        )
        return response

    def delete(self,key):
        """Delete the object."""
        response = self.s3.delete_object(
            Bucket=self.bucketname,
            Key=key,
        )
        return response

S3Object = S3()
