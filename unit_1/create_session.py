'''
Having explored the essentials of securely managing AWS sessions and the importance of not embedding your credentials 
directly in your code, it's now time for a hands-on challenge. Your task is to establish a boto3 session that explicitly 
sets the region to "us-west-2". This exercise underscores the significance of keeping your AWS access secure and demonstrates 
how to configure regional preferences for your AWS operations.
'''

import boto3

# TODO: Create a boto3 session with the region set to "us-west-2".
session = boto3.Session(
    region_name='us-west-2'
)