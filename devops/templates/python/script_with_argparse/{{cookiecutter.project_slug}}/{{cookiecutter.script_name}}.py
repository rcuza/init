#!/usr/bin/env python
# encoding: utf-8

"""
{{cookiecutter.script_name}}.py
Created by {{cookiecutter.author_name}} on {{cookiecutter.date}}.
Copyright (c) {{cookiecutter.date.split("-")[0]}}, {{cookiecutter.organization_name}}. All rights reserved.

Template built for python v2.7 and v3.6
"""

from __future__ import absolute_import, division, print_function

import argparse
import logging
import sys

PROGRAM_NAME = '{{cookiecutter.script_name}}.py'

VERINFO = '{{cookiecutter.script_version}}'

LICENSE = "ISC License"
LICENSE_URL = "https://choosealicense.com/licenses/isc/"

HELP_MESSAGE = """
The help message goes here.
"""


def parse_args():
    """
    Puase any command line arguments.
    """
    parser = argparse.ArgumentParser(
        prog=PROGRAM_NAME,
        description=HELP_MESSAGE)
    # Determine verbosity (optional argument)
    parser.add_argument(
        "-v", "--verbose",
        help="increase output verbosity",
        action="store_true",
        default=False)
    # Example of mantitory positional argument
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
