# Starts the EC2 instances
 
import boto3
region = 'us-east-1'
instances = ['i-12345', 'i-2345']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))