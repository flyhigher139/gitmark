#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User

import requests

from gitmark import celery_app
from main import functions


@celery_app.task(name='gitmark.test_celery')
def test_celery():
    print 'hello, world'

@celery_app.task(name='gitmark.import_starred_repos')
def import_github_starred_repos(github_username, gitmark_username):
    cur_user = User.objects.get(username=gitmark_username)
    page = 1
    api = functions.build_github_starred_api(github_username, page)
    res = requests.get(api)
    starred_repos = res.json()
    print page

    while len(starred_repos) > 0:
        functions.import_repos(starred_repos, cur_user)

        page += 1
        api = functions.build_github_starred_api(github_username, page)
        res = requests.get(api)
        starred_repos = res.json()
        print page
    # print cur_user.id

