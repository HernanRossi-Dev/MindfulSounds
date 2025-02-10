import boto3
from botocore.exceptions import NoCredentialsError, ClientError

def create_s3_bucket(bucket_name, region=None):
    try:
        s3_client = boto3.client('s3', region_name=region)
        if region is None:
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f'Bucket {bucket_name} created successfully.')
    except ClientError as e:
        print(f'Error creating bucket: {e}')
    except NoCredentialsError:
        print('Credentials not available.')

def upload_file_to_s3(file_name, bucket_name, object_name=None):
    if object_name is None:
        object_name = file_name
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
        print(f'File {file_name} uploaded to {bucket_name}/{object_name}.')
    except ClientError as e:
        print(f'Error uploading file: {e}')

def list_audio_files(bucket_name):
    s3_client = boto3.client('s3')
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in response:
            for obj in response['Contents']:
                print(obj['Key'])
        else:
            print('No audio files found in the bucket.')
    except ClientError as e:
        print(f'Error listing files: {e}')