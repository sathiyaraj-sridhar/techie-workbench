"""
SES model
"""

# Import community modules.
import boto3
import botocore

# Import custom modules.
from config import appconf


class SESModel:
    """Manage SES."""
    def __init__(self):
        """Initializer. """
        self.source = appconf['ses']['source']
        self.conn = self.connect()

    def connect(self):
        """Instantiate SES service connection."""
        try:
            config = botocore.config.Config(connect_timeout=2,read_timeout=2)
            self.ses = boto3.client('ses',config=config)
            return {'status':'success','message':'Connection successful.'}
        except Exception as error:
            return {'status':'failure','message':str(error)}

    def reconnect(self):
        """Re-Instantiate SES service connection."""
        self.ses.close()
        self.conn = self.connect()

    def send_email(self,destination,subject,body):
        """Send Email."""
        response = self.ses.send_email(
            Source=self.source,
            Destination={
                'ToAddresses': [destination]
            },
            Message={
                'Subject': {'Data': subject, 'Charset': 'UTF-8'},
                'Body': {
                    'Text': {'Data': body, 'Charset': 'UTF-8'}
                }
            }
        )
        return response

SES = SESModel()
