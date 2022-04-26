import os

# Common settings

pass


# Settings on windows machine (development)

if os.name == 'nt':
    STATIC_ROOT = ''


# Settings on linux server (deployment)

if os.name == 'posix':
    STATIC_ROOT = '/home/SnipselBucket/SnipselBucket/snipselbucketsite/static'