import boto3
import requests
import sys

url = sys.argv[1]
bucket = sys.argv[2]
expires = int(sys.argv[3])

filename = url.split('/')[-1]

# ✅ Properly download binary image
response = requests.get(url)
with open(filename, 'wb') as f:
    f.write(response.content)

# Upload to S3
s3 = boto3.client('s3', region_name='us-east-1')
s3.upload_file(filename, bucket, filename)

# Generate presigned URL
presigned_url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket, 'Key': filename},
    ExpiresIn=expires
)

print("Presigned URL:", presigned_url)

