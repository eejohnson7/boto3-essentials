'''
You've mastered the setup of a client with custom retry strategies in Boto3! Now, let's put your skills to the test. 
Configure a Boto3 S3 client using a specific custom retry strategy: set the number of retries to 5 and use the standard 
retry mode.
'''

import boto3
from botocore.config import Config

# TO DO: Setup a boto3 S3 client with a custom retry strategy: set 'max_attempts' to 5 and 'mode' to 'standard'
config_with_retry = Config(
    retries={
        'max_attempts': 5,
        'mode': 'standard',
    }
)

s3 = boto3.client('s3', config=config_with_retry)

# Retrieve the list of S3 buckets
response = s3.list_buckets()
print(response['Buckets'])