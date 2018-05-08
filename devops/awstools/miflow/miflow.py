#!/usr/bin/env python3
# encoding: utf-8

"""
miflow.py
Created by Raúl Cuza on 2018-05-08.
Copyright (c) Raúl Cuza. All rights reserved.

script to assist in the discovery and management of AWS amis
"""

import argparse
import logging
import sys

import boto3

PROGRAM_NAME = '${TM_NEW_FILE_BASENAME}.py'

VERINFO = '0.0.0'

LICENSE = "ISC License"
LICENSE_URL = "https://choosealicense.com/licenses/isc/"

HELP_MESSAGE = """
machine image work flow assistant
"""


def delete_ami(ami_id, safety_check=False):
    """
    take the ami_id and deregister it and delete the backing snapshot
    """
    snapshot_id = get_snapshot_id(ami_id)
    logging.debug("snapshot_id is %s", snapshot_id)
    if safety_check:
        if snapshot_id and isinstance(snapshot_id, string_types):
            response_ami = delete_ami_deregister(ami_id)
            response_snapshot = delete_ami_del_snapshot(snapshot_id)
            results = [
                response_ami,
                response_snapshot,
                ]
        else:
            logging.warn("something is wrong with %s", ami_id)
            logging.warn("snapshot id must be a string: %s", snapshot_id)
            results = False
    else:
        logging.info("safety check enabled. "
                     "ami and snapshot were not removed.")
        print("ami id: ", ami_id)
        print("snapshot id: ", snapshot_id)
        results = False
    return results


def delete_ami_deregister(ami_id):
    """
    deregister ami
    """
    logging.debug("deregistering image %s", ami_id)
    ec2 = boto3.resource('ec2')
    image = ec2.Image(ami_id)
    response_ami = image.deregister(DryRun=False)
    logging.info("image deregister response: %s", response_ami)
    return response_ami


def delete_ami_del_snapshot(snapshot_id):
    """
    delete snapshot_id
    """
    logging.debug("deleting snapshot %s", snapshot_id)
    client = boto3.client('ec2')
    response_snapshot = client.delete_snapshot(
        SnapshotId=snapshot_id,
        DryRun=False,
        )
    logging.info("snapshot delete response: %s", response_snapshot)
    return response_snapshot


def describe_images(ami_ids):
    """
    find the image descriptions of a one or more amis and
    return a list of dictionaries
    """
    if isinstance(ami_ids, str):
        ami_ids = [ami_ids]
        logging.debug("ami_ids was a string: %s", ami_ids)
    else:
        logging.debug("ami_ids is a list: %s", ami_ids)
    client = boto3.client('ec2')
    results = client.describe_images(ImageIds=ami_ids)
    return results

def get_snapshot_id(ami_ids):
    """
    get the snapshot_id(s) of the first Ebs of ami_id(s)
    """
    images_info = describe_images(ami_ids)
    s_id = [i['BlockDeviceMappings'][0]['Ebs']['SnapshotId'] for i in images_info['Images']]
    if len(s_id) == 1:
        results = s_id[0]
    else:
        results = s_id
    return results

def share_snapshot_with(aws_accounts, ss_id):
    """
    share ami_id (snapshot and ami) with awsaccount

    assume default aws account is account sharing ami

    TODO share AMI too
    TODO verify before sharing status of share
    TODO verify share status after (for DEBUG)
    """
    if isinstance(aws_accounts, str):
        aws_accounts = [aws_accounts]
        logging.debug("aws_accounts was a string: %s", aws_accounts)
    else:
        logging.debug("aws_accounts is a list: %s", aws_accounts)
    client = boto3.client('ec2')
    response = client.modify_snapshot_attribute(
        Attribute='createVolumePermission',
        DryRun=False,
        OperationType='add',
        SnapshotId=ss_id,
        UserIds=aws_accounts,
    )
    return response


# UI functions
def query_yes_no(question, default="no"):
    """Ask a yes/no question via input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [yes/no] "
    elif default == "yes":
        prompt = " [YES/no] "
    elif default == "no":
        prompt = " [yes/NO] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("unknown response. assuming " + default + "\n")
            return valid[default]


def parse_args():
    """
    Puase any command line arguments.
    """
    parser = argparse.ArgumentParser(
        prog=PROGRAM_NAME,
        description=HELP_MESSAGE)
    parser.add_argument(
        "-v", "--verbose",
        help="increase output verbosity",
        action="store_true",
        default=False)
    parser.add_argument(
        "echo",
        help="This is a positional argument",
        nargs='+')
    args = parser.parse_args()

    return args


def main():
    """
    Steps if script is run directly
    """
    args = parse_args()

    # Change log level if using verbose
    if args.verbose:
        logging.basicConfig(
            format="%(levelname)s: %(message)s",
            level=logging.DEBUG)
        logging.info("Verbose logging.")
        logging.debug("Supplied Arguments: %s", args)
        logging.debug("Version: %s", VERINFO)
    else:
        logging.basicConfig(format="%(message)s", level=logging.INFO)

    print(args.echo)


if __name__ == "__main__":
    sys.exit(main())
