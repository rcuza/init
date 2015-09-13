#!/usr/bin/env python
# encoding: utf-8
"""
${TM_NEW_FILE_BASENAME}.py
Created by ${TM_FULLNAME} on ${TM_DATE}.
Copyright (c) ${TM_YEAR} ${TM_ORGANIZATION_NAME}. All rights reserved.

Template built on python v2.7
"""

import sys
import argparse


help_message = '''
The help message goes here.
'''


def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser(
            prog = '${TM_NEW_FILE_BASENAME}.py',
            description = __doc__)
    # Determine verbosity (optional argument)
    parser.add_argument("-v", "--verbose",
            help = "increase output verbosity",
            action = "store_true",
            default = False)
    # Example of mantitory positional argument
    parser.add_argument("echo",
            help="This is a positional argument",
            nargs='+')
    args = parser.parse_args()

    if args.verbose:
        print "verbosity turned on"

    print args.echo

    pass


if __name__ == "__main__":
    sys.exit(main())
