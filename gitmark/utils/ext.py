#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings

import qiniu

QINIU_ACCESS_KEY = settings.GITMARK['QINIU']['access_key']
QINIU_SECRET_KEY = settings.GITMARK['QINIU']['secret_key']
QINIU_BUCKET_NAME = settings.GITMARK['QINIU']['bucket_name']
QINIU_URL = settings.GITMARK['QINIU']['base_url']

def qiniu_fetch_img(img_url, img_name):
	q = qiniu.Auth(QINIU_ACCESS_KEY, QINIU_SECRET_KEY)
	token = q.upload_token(QINIU_BUCKET_NAME)

	bucket = qiniu.BucketManager(q)
	ret, info = bucket.fetch(img_url, QINIU_BUCKET_NAME, img_name)

	if not ret:
		return None

	key = ret.get('key')
	return QINIU_URL + key



