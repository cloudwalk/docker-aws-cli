#!/usr/bin/python
""" Tool to setup AWS CLI.
"""
import os
import sys
from subprocess import check_output

def setup_s3(s3_access_key, s3_secret_key):
    """Create S3 configuration file."""
    home = os.path.expanduser("~")
    aws_dir = os.path.join(home, '.aws')
    if not os.path.exists(aws_dir):
        os.makedirs(aws_dir)

    # Write config file
    with open(os.path.join(aws_dir, 'config'), 'w') as f:
        f.write('[default]\n')

    # Write to disk S3cmd config file
    with open(os.path.join(aws_dir, 'credentials'), 'w') as f:
        credentials = '[default]\naws_access_key_id = %s\naws_secret_access_key = %s\n' % (s3_access_key, s3_secret_key)
        f.write(credentials)

def execute(command):
    """ Execute external host command and print it's output."""
    output = check_output(command)
    print output.rstrip()

def print_usage():
    print "Usage: docker run -e S3_ACCESS_KEY=[PUT KEY HERE] -e S3_SECRET_KEY=[PUT KEY HERE] cloudwalk/aws [PUT COMMAND HERE]"

if __name__ == '__main__':
    # Get  expected environment variables
    access_key = os.getenv('S3_ACCESS_KEY')
    secret_key = os.getenv('S3_SECRET_KEY')
    if access_key is None or secret_key is None:
        print_usage()
        sys.exit(1)

    # Create AWS config file
    setup_s3(access_key, secret_key)

    # Execute aws command appended by whatever arguments is passed to this script
    command = ['aws'] + sys.argv[1:]
    execute(command)
