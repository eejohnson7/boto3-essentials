'''
Ready to take control? For this task, initialize an EC2 resource in AWS using Boto3. You will do this twice: first, by 
leveraging the default session, and second, by creating a custom session set to the 'us-west-2' region. This exercise will 
solidify your understanding of handling AWS resources with Python. Let’s make it happen!
'''

import boto3

# TODO: Use boto3 to initialize an EC2 resource with the default session.
resource = boto3.resource('ec2')

# TODO: Create a custom session targeting the 'us-west-2' region.
session = boto3.Session(
    region_name="us-west-2"
)

# TODO: Use the custom session you created to initialize another EC2 resource.
custom_resource = session.resource('ec2')