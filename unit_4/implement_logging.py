'''
As you progress with Boto3, understanding and implementing logging is crucial for diagnosing and troubleshooting AWS 
service interactions. This exercise focuses on configuring logging for a Boto3 S3 client operation. Your task is to set up 
logging to capture and display detailed DEBUG information specifically for S3 interactions.

Hint: Leverage Python's logging module for configuration and employ boto3.set_stream_logger() to fine-tune logging for 
the S3 service at the DEBUG level.
'''

import boto3
import logging

# TODO: Set up logging to capture DEBUG information for S3 client interactions
# Hint: Configure logging using Python’s logging module and boto3.set_stream_logger() for S3 at DEBUG level
boto3.set_stream_logger(name='botocore.client.S3', level=logging.DEBUG)

s3 = boto3.client('s3')

# Attempt an S3 operation to generate and capture detailed logs
try:
    s3.list_buckets()
except Exception as e:
    # Use logging to report errors
    logging.error("An error occurred: ", exc_info=e)