# -*- coding: utf-8 -*-
# flake8: noqa
import os
import subprocess

from settings import ACCESS_KEY, BUCKET_NAME, SECRET_KEY


def uploader(key):
    localfile = os.path.join(os.getcwd(), 'videos', key)
    try:
        subprocess.call(['./qshell', 'account', ACCESS_KEY, SECRET_KEY])
        subprocess.call(['./qshell', 'rput', BUCKET_NAME, key, localfile])
        print('{0} upload finished'.format(key))
    except Exception as e:
        print('{0} upload failed: {1}'.format(key, e))
