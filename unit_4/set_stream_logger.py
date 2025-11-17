'''
Following your progress on the hands-on tasks, you're doing an excellent job! In this exercise, you're introduced to a 
Python script that leverages the Boto3 library for AWS S3 operations. The script sets up a resource for S3, creates a bucket, 
and lists all available buckets. Your task is to elevate the existing logging level from the default WARNING to DEBUG. 
Here's a hint: leverage Python's logging module to configure the level to DEBUG. This alteration will provide more descriptive 
log outputs for your AWS interactions.
'''

import boto3
import logging

# Basic logging setup with WARNING level
logging.basicConfig(level=logging.DEBUG)

# Initialize a boto3 S3 resource
s3 = boto3.resource('s3')

# Create a new bucket
s3.create_bucket(Bucket='my-debug-logging-bucket')

# Iteratively print all bucket names
for bucket in s3.buckets.all():
    print(bucket.name)