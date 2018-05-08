#!/usr/bin/env python
# encoding: utf-8

"""
mifind.py
Created by Raúl Cuza on 2018.05.08.
Copyright (c) 2018. All rights reserved.

Template built for python v2.7 and v3.6
"""

from __future__ import absolute_import, division, print_function

import argparse
import json
import logging
import sys

import boto3

PROGRAM_NAME = 'mifind.py'

VERINFO = '0.2.0'

LICENSE = "ISC License"
LICENSE_URL = "https://choosealicense.com/licenses/isc/"

HELP_MESSAGE = """
find which launch configs and ec2 are using a particular ami (outputs json)
"""


def find_amis_w_tags(tags):
    """
    take a dictionary of tags and return a list of amis
    that match
    """
    return []


def find_asg_using_amis(ami_ids):
    """
    take a list of ami ids and return a dictionary of
    launch configs that use them
    """
    # ref: return = { ami_id : "lc_arns":[]}
    ami_ids = listify(ami_ids)
    result = {id: [] for id in ami_ids}

    client_asg = boto3.client('autoscaling')
    lc = client_asg.describe_launch_configurations()

    for a_lc in lc['LaunchConfigurations']:
        if a_lc['ImageId'] in ami_ids:
            result[a_lc['ImageId']].append(a_lc['LaunchConfigurationARN'])
    return result


def find_ec2_using_amis(ami_ids):
    """
    take a list of ami ids and return a dictionary of
    ec2 and launch_configs that use the amis
    """
    # ref: return = { "ami_id" : "ec2":[]}
    ami_ids = listify(ami_ids)
    result = {id: [] for id in ami_ids}

    client = boto3.client('ec2')
    image_id_filter = {'Name': 'image-id', 'Values': ami_ids}
    filter = [image_id_filter]

    response = client.describe_instances(Filters=filter)
    for res in response['Reservations']:
        for instance in res['Instances']:
            result[instance['ImageId']].append(instance['InstanceId'])

    return result


def listify(var):
    """
    take var and return it as a list
    """
    if isinstance(var, str):
        result = [var]
        logging.debug("input was a string: %s", result)
    elif isinstance(var, dict):
        result = [var]
        logging.debug("input was a dict: %s", result)
    else:
        result = var
        logging.debug("input is a list: %s", result)
    return result


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
        "ami_ids",
        help="ami_id [ami_id, [...]]",
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

    lc_results = find_asg_using_amis(args.ami_ids)
    ec2_results = find_ec2_using_amis(args.ami_ids)

    output = {}
    for ami_id in args.ami_ids:
        output[ami_id] = {
            'lcs': lc_results[ami_id],
            'ec2': ec2_results[ami_id],
            }
    print(json.dumps(output))


if __name__ == "__main__":
    sys.exit(main())
