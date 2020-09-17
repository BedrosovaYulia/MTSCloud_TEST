import sys

sys.path.append("/mnt/volume/packages/venv/lib/python3.8/site-packages/")

import os
import boto3
import json


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

    # Загрузить объекты в бакет

    ## Из строки
    s3.put_object(Bucket=os.environ['bucket'], Key=rq['args']['email'], Body=str(
        json.dumps(rq['args'])))

    return rq, None
