#!/usr/bin/env python
# encoding: utf-8
"""
${TM_NEW_FILE_BASENAME}.py
Created by ${TM_FULLNAME} on ${TM_DATE}.
Copyright (c) ${TM_YEAR}, ${TM_ORGANIZATION_NAME}. All rights reserved.

Template built on python v2.7
"""
LICENSE = """
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""


import argparse
import sys


help_message = '''
The help message goes here.
'''


def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = argparse.ArgumentParser(
            prog='${TM_NEW_FILE_BASENAME}.py',
            description=__doc__)
    # Determine verbosity (optional argument)
    parser.add_argument("-v", "--verbose",
            help="increase output verbosity",
            action="store_true",
            default=False)
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
