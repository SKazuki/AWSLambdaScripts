import boto3
import time
from botocore.client import ClientError

# Enter the region your instances are in, e.g. 'us-east-1'
region = 'XXXXXXX'

# Enter your instances here: ex. ['X-XXXXXXXX', 'X-XXXXXXXX']
instances = ['X-XXXXXXX']

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name=region)
    # Try 2 times
    for i in range(1, 3):
        try:
            ec2.start_instances(InstanceIds=instances)
            print 'started your instances: ' + str(instances)
            return True
        except ClientError as e:
            print str(e)
        time.sleep(1)
    raise Exception('cannot start instance ' + str(instances))
