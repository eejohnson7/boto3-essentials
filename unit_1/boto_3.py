'''
Dive into Boto3's capabilities by running a provided script to explore the available AWS services and resources, all 
without writing any code. This task highlights the extensive array of services accessible through low-level clients versus 
the select few available as high-level resources, demonstrating Boto3's adaptability across AWS's broad service landscape. 
Click the Run button to see the list of services and resources, gaining insight into how Boto3 enables both detailed control 
and simplified management of AWS services.

Important Note: Running scripts can alter the filesystem's state or modify the resources in our AWS simulator. To revert to 
the initial state, you can use the reset button located in the top right corner. However, keep in mind that resetting will 
erase any code changes. To preserve your code during a reset, consider copying it to the clipboard.
'''

import boto3

# Create a Boto3 session
session = boto3.session.Session()

# List all available services under client interface
client_services = session.get_available_services()
print("Available services with client interface:")
for service in sorted(client_services):
    print(service)

# List all available services under resource interface
resource_services = session.get_available_resources()
print("\nAvailable services with resource interface:")
for service in sorted(resource_services):
    print(service)