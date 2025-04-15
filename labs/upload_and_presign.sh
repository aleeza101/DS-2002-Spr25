#!/bin/bash

FILE=$1
BUCKET=$2
EXPIRES=$3

# Upload file
aws s3 cp $FILE s3://$BUCKET/

# Generate presigned URL
aws s3 presign --expires-in $EXPIRES s3://$BUCKET/$(basename $FILE)

