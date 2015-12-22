# Docker AWS CLI

This is a minimalist Docker container with [AWS CLI](http://aws.amazon.com/cli/)
installed. The image has 76.97 MB.

## Usage

You just need to pass your AWS credentials as environment variables to the container:

```
docker run -e S3_ACCESS_KEY=[PUT KEY HERE] -e S3_SECRET_KEY=[PUT KEY HERE] cloudwalk/aws [PUT COMMAND HERE]
```
