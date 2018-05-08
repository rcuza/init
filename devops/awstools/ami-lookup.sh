#!/bin/sh

# LICENSE: ISC License
# url: https://choosealicense.com/licenses/isc/
# Copyright (c) 2018, Raúl Cuza

yell() { echo "$0: $*" >&2; }
die() { yell "$*"; exit 111; }
try() { "$@" || die "cannot $*"; }

: "${AWS_REGION:="us-east-1"}"

# TODO get it to just show the latest AMI
# how to find centos ami according to https://wiki.centos.org/Cloud/AWS
centos6_table () {
  try aws --region ${AWS_REGION} ec2 describe-images \
        --owners aws-marketplace \
        --filters Name=product-code,Values=6x5jmcajty9edm3f211pqjfn2 \
    | jq '.Images[] | {Date: .CreationDate, Description: .Description, ami_id: .ImageId, snapshot_id: .BlockDeviceMappings[0].Ebs.SnapshotId, volume_size: .BlockDeviceMappings[0].Ebs.VolumeSize,  Name: .Name}'
}

centos7_table () {
  try aws --region ${AWS_REGION} ec2 describe-images \
        --owners aws-marketplace \
        --filters Name=product-code,Values=aw0evgkw8e5c1q413zgy5pjce \
    | jq '.Images[] | {Date: .CreationDate, Description: .Description, ami_id: .ImageId, snapshot_id: .BlockDeviceMappings[0].Ebs.SnapshotId, volume_size: .BlockDeviceMappings[0].Ebs.VolumeSize,  Name: .Name}'
}

ubuntu_lookup () {
  : "${ubuntu_version:="ubuntu"}"
  name=$(\
      try aws --region ${AWS_REGION} ec2 describe-images --owners 099720109477 \
          --filters Name=root-device-type,Values=ebs \
                    Name=architecture,Values=x86_64 \
                    Name=name,Values="*hvm-ssd/${ubuntu_version}-*" \
      | awk -F ': ' '/"Name"/ { print $2 | "sort" }' \
      | tr -d '",' \
      | tail -1)

  ami_id=$(\
      try aws --region ${AWS_REGION}  ec2 describe-images --owners 099720109477 \
          --filters Name=name,Values="$name" \
      | awk -F ': ' '/"ImageId"/ { print $2 }' \
      | tr -d '",')

  echo "${name}"
  echo "${ami_id}"
}

case ${1} in
  "ubuntu")
    ubuntu_lookup
    ;;
  "zesty")
    ubuntu_version="ubuntu-zesty-17.04"
    ubuntu_lookup
    ;;
  "xenial")
    ubuntu_version="ubuntu-xenial-16.04"
    ubuntu_lookup
    ;;
  "vivid")
    ubuntu_version="ubuntu-vivid-15.04"
    ubuntu_lookup
    ;;
  "trusty")
    ubuntu_version="ubuntu-trusty-14.04"
    ubuntu_lookup
    ;;
  "centos7")
    centos7_table
    ;;
  "centos6")
    centos6_table
    ;;
  *)
    description="choose one: centos6, centos7 zesty (17.04), xenial (16.04), vivid (15.04), trusty (14.04)"
    usage="* usage example: ami-lookup.sh xenial"
    defaults="* region: ${AWS_REGION}"
    printf "%s\n%s\n%s\n" "${description}" "${usage}" "${defaults}"
esac
