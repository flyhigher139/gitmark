#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings

import requests
from requests_oauthlib import OAuth2Session, OAuth2

from gitmark import github_apis
from utils.ext import qiniu_fetch_img
from . import models

client_id = settings.GITMARK['GITHUB']['client_id']
client_secret = settings.GITMARK['GITHUB']['client_secret']
authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'

def github_auth(request):
    """Step 1: User Authorization.

    Redirect the user/resource owner to the OAuth provider (i.e. Github)
    using an URL with a few key OAuth parameters.
    """
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
    github = OAuth2Session(client_id)
    authorization_url, state = github.authorization_url(authorization_base_url)

    # State is used to prevent CSRF, keep this for later.
    request.session['oauth_user_state'] = state
    return redirect(authorization_url)


# Step 2: User authorization, this happens on the provider.


def github_callback(request):
    """ Step 3: Retrieving an access token.

    The user has been redirected back from the provider to your registered
    callback URL. With this redirection comes an authorization code included
    in the redirect URL. We will use that to obtain an access token.
    """

    github = OAuth2Session(client_id, state=request.session['oauth_user_state'])
    token = github.fetch_token(token_url, client_secret=client_secret,
                               authorization_response=request.get_full_path())

    # At this point you can fetch protected resources but lets save
    # the token and show how this is done from a persisted token
    # in /profile.
    request.session['oauth_user_token'] = token

    # response to callback as follow:
    if request.session['oauth_callback_type'] == 'register':
        return github_register_behavior(request)

    if request.session['oauth_callback_type'] == 'login':
        return github_login_behavior(request)

    if request.session['oauth_callback_type'] == 'link_github':
        return github_link_account_behavior(request)

    url = reverse('main:admin_index')
    return redirect(url)

def github_register_behavior(request):
    url = github_apis.auth_user()
    auth = OAuth2(client_id=client_id, token=request.session['oauth_user_token'])
    res = requests.get(url, auth=auth)
    if res.status_code != 200:
        msg = 'GitHub authorization failed'
        url = reverse('accounts:register')
        messages.add_message(request, messages.ERROR, msg)
        return redirect(url)

    github_user = res.json()
    username = github_user.get('login')
    email = github_user.get('email')
    github_url = github_user.get('html_url')
    github_avatar_url = github_user.get('avatar_url')

    users = models.Account.objects.filter(github_username=username)
    if len(users) > 0:
        msg = 'You have registered with Github'
        messages.add_message(request, messages.ERROR, msg)
        url = reverse('accounts:login')
        return redirect(url)

    def create_user(username, email, password):
        try:
            user = User.objects.create_user(username, email, password)
            user.save()

            return user

        except IntegrityError:
            from random import random, randint
            username = username + str(randint(1, 1000))
            return create_user(username, email, password)

    avatar_name = 'github_avatar_{0}.jpeg'.format(username)
    avatar_url = qiniu_fetch_img(github_avatar_url, avatar_name)

    user = create_user(username, email, 'password')
    account = user.account
    account.github_username = username
    account.github = github_url
    account.avatar = avatar_url
    account.save()

    user = authenticate(token=request.session['oauth_user_token'])
    login(request, user)

    # url = reverse('accounts:login')
    url = reverse('main:admin_index')
    return redirect(url)

def github_login_behavior(request):
    user = authenticate(token=request.session['oauth_user_token'])

    if user is not None:
        if user.is_active:
            login(request, user)
            url = request.GET.get('next', None)
            if not url:
                url = reverse('main:admin_index')
            return redirect(url)
        else:
            msg = 'The user is disabled'
            messages.add_message(request, messages.WARNING, msg)
            return self.get(request, form)
    else:
        msg = 'Invalid login, user does not exist'
        messages.add_message(request, messages.ERROR, msg)
        url = reverse('accounts:register')
        return redirect(url)

def github_link_account_behavior(request):
    url = github_apis.auth_user()
    auth = OAuth2(client_id=client_id, token=request.session['oauth_user_token'])
    res = requests.get(url, auth=auth)
    if res.status_code != 200:
        msg = 'GitHub authorization failed'
        url = reverse('accounts:register')
        messages.add_message(request, messages.ERROR, msg)
        return redirect(url)

    github_user = res.json()
    username = github_user.get('login')
    email = github_user.get('email')
    github_url = github_user.get('html_url')
    github_avatar_url = github_user.get('avatar_url')

    avatar_name = 'github_avatar_{0}.jpeg'.format(username)
    avatar_url = qiniu_fetch_img(github_avatar_url, avatar_name)

    account = request.user.account
    account.github_username = username
    account.github = github_url
    account.avatar = avatar_url
    account.save()
    
    url = reverse('main:admin_index')
    return redirect(url)

