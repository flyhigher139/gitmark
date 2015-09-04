#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.conf import settings

import requests

from gitmark import celery_app
from main import functions

app_user = settings.GITMARK['GITHUB']['app_user']
app_pass = settings.GITMARK['GITHUB']['app_pass']


@celery_app.task(name='gitmark.test_celery')
def test_celery():
    print 'hello, world'

@celery_app.task(name='gitmark.import_starred_repos')
def import_github_starred_repos(github_username, gitmark_username):
    cur_user = User.objects.get(username=gitmark_username)
    page = 1
    api = functions.build_github_starred_api(github_username, page)
    res = requests.get(api, auth=(app_user, app_pass))

    # print app_user, app_pass, res.status_code
    # res = requests.get(api)
    starred_repos = res.json()
    print page

    # GitHub API rate limit exceeded 
    if not isinstance(starred_repos, list):
        print 'GitHub API rate limit exceeded '
        return

    while len(starred_repos) > 0:
        functions.import_repos(starred_repos, gitmark_user=cur_user)

        page += 1
        api = functions.build_github_starred_api(github_username, page)
        res = requests.get(api, auth=(app_user, app_pass))
        # res = requests.get(api)
        if res.status_code != 200:
            print 'GitHub API rate limit exceeded '
            return
        starred_repos = res.json()
        print page
    # print cur_user.id

@celery_app.task(name='gitmark.import_repos')
def import_github_repos(github_username):
    page = 1
    api = functions.build_github_starred_api(github_username, page)
    res = requests.get(api, auth=(app_user, app_pass))
    starred_repos = res.json()
    print page

    # GitHub API rate limit exceeded 
    if not isinstance(starred_repos, list):
        print 'GitHub API rate limit exceeded'
        return

    while len(starred_repos) > 0:
        functions.import_repos(starred_repos)

        page += 1
        api = functions.build_github_starred_api(github_username, page)
        res = requests.get(api, auth=(app_user, app_pass))
        if res.status_code != 200:
            print 'GitHub API rate limit exceeded '
            return
        starred_repos = res.json()
        print page
#     # print cur_user.id

