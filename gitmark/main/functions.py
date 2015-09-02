#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import models

def build_github_starred_api(username, page, per_page=100):
            return 'https://api.github.com/users/{0}/starred?page={1}&per_page={1}'.format(username, page, per_page)

def import_repos(github_starred_repos, gitmark_user):
    for starred_repo in github_starred_repos:
        language, created = models.Language.objects.get_or_create(name=(starred_repo.get('language') or 'unknown'))

        repo, created = models.Repo.objects.get_or_create(full_name=starred_repo.get('full_name'), 
            defaults={
                'name' : starred_repo.get('name'),
                'link' : starred_repo.get('html_url'),
                'author' : starred_repo.get('owner').get('login'),
                'author_link' : starred_repo.get('owner').get('html_url'),
                'desc' : starred_repo.get('description'),
                'language' :language
            })

        repo.starred_users.add(gitmark_user)

####################################
# legacy_oauth example
####################################

# def legacy_oauth():
#     username = 'gevin'
#     password = 'gevin'
#     client_id = '8UbOpkcldxGI3US78NcnROyxma3BUP2P595T4Hl6'
#     client_secret = 'exi0Al9U3mx2JnINSUfmcb9adLz1NZNbuAbO56C1lHGpNh4BeKJSV6j7QBPfhJJMs9cOVqVYuCunYbeNjm64O14FukRP3eMz4KS6rG8tedGhYpRvI91JlvrgdkcbBVIU'
#     oauth = OAuth2Session(client=LegacyApplicationClient(client_id=client_id))
#     token = oauth.fetch_token(token_url=token_url,
#         username=username, password=password, client_id=client_id,
#         client_secret=client_secret)

#     url = 'http://localhost:8000/api/user/images/'
#     auth = OAuth2(client_id=client_id, token=token)
#     res = requests.get(url, auth=auth)
#     return res.text