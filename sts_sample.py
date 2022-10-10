# Sample code work with
# Security Token Service  : sts
# Author : Babak Jahangiri


import boto3

sts_client = boto3.client('sts', endpint_url = 'https://site.com:9000', aws_access_key_id= 'access key id', aws_secret_access_key='secret key', config= config, region_name='us-east-1')

