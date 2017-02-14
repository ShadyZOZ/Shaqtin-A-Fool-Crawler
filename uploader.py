# -*- coding: utf-8 -*-
# flake8: noqa
import os

from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config

from settings import ACCESS_KEY, SECRET_KEY, BUCKET_NAME


def uploader(key):
    print(key)
    q = Auth(ACCESS_KEY, SECRET_KEY)
    token = q.upload_token(BUCKET_NAME, key, 3600)
    localfile = os.path.join(key, '/videos/') + key
    ret, info = put_file(token, key, localfile)
    print(info)
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)
