#!/bin/bash
# thank you http://www.jamesransom.net/uploading-a-file-using-curl-to-s3-aws/
bucket=$1
file=$2
resource="/${bucket}/${file}"
contentType="application/x-itunes-ipa"
dateValue=$(date -u  +"%a, %d %b %Y %H:%M:%S +0000")
stringToSign="PUT\n\n${contentType}\n${dateValue}\n${resource}"
s3Key=${AWS_ACCESS_KEY_ID:-KEYHERE}
s3Secret=${AWS_SECRET_ACCESS_KEY:-SECRETHERE}
echo "SENDING TO S3"
signature=$(echo -en ${stringToSign} | openssl sha1 -hmac ${s3Secret} -binary | base64)
curl -vv -X PUT -T "${file}" \
 -H "Host: ${bucket}.s3.amazonaws.com" \
 -H "Date: ${dateValue}" \
 -H "Content-Type: ${contentType}" \
 -H "Authorization: AWS ${s3Key}:${signature}" \
 https://${bucket}.s3.amazonaws.com/${file}
