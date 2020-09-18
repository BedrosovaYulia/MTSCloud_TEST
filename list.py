import sys

sys.path.append("/mnt/volume/packages/venv/lib/python3.8/site-packages/")

import json
import boto3
import os

def Main(rq):
    #print(rq)
    
    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        #endpoint_url='https://storage.yandexcloud.net',
        endpoint_url='https://s3.rusonyx.ru',
        aws_access_key_id=os.environ['key_id'],
        aws_secret_access_key=os.environ['access_key'],
        )
    
    # Получаем данные
    messagelist = dict()
    
    for key in s3.list_objects(Bucket=os.environ['bucket'], Prefix='data')['Contents']:
        get_object_response = s3.get_object(
            Bucket=os.environ['bucket'], Key=key['Key'])
        messagelist[key['Key']] = json.loads(
            get_object_response['Body'].read().decode())

    return messagelist, None
