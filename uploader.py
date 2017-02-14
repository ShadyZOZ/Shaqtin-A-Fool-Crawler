# -*- coding: utf-8 -*-
# flake8: noqa

from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config

from .settings import ACCESS_KEY, SECRET_KEY, BUCKET_NAME


class Uploader():
    q = Auth(ACCESS_KEY, SECRET_KEY)

    def upload(key, localfile):
        token = q.upload_token(BUCKET_NAME, key, 3600)
        ret, info = put_file(token, key, localfile)
        print(info)
        assert ret['key'] == key
        assert ret['hash'] == etag(localfile)
