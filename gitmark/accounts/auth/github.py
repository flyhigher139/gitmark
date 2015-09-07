#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User

import requests
from requests_oauthlib import OAuth2Session, OAuth2

from gitmark import github_apis

class GitHubBackend(object):
    def authenticate(self, token=None):
        url = github_apis.auth_user()
        auth = OAuth2(client_id=client_id, token=token)
        res = requests.get(url, auth=auth)
        if res.status_code != 200:
            msg = 'GitHub authorization failed'
            url = reverse('accounts:register')
            messages.add_message(request, messages.ERROR, msg)
            return redirect(url)

        github_user = res.json()
        github_username = github_user.get('login')

        try:
            user = User.objects.get(account__github_username=github_username)
            return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None