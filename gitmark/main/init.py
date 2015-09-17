#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from accounts import forms
from . import models

class GitMarkInitView(View):
    template_name = 'accounts/simple_form.html'
    def get(self, request, form=None):
        initialized = False

        try:
            initialization = models.GitMarkMeta.objects.get(key='initialization')
            initialized = initialization.flag
        except models.GitMarkMeta.DoesNotExist:
            initialized = False
        
        if initialized:
            url = reverse('main:admin_index')
            return redirect(url)


        if not form:
            form = forms.RegisterForm()
        data = {'form':form}
        data['title'] = 'System Initialization'
        data['heading'] = 'Create Superuser'
        return render(request, self.template_name, data)

    def post(self, request):
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_superuser(username, email, password)

            initialization, created = models.GitMarkMeta.objects.get_or_create(key='initialization')
            initialization.flag = True
            initialization.save()

            msg = 'Successfully Initialized'
            messages.add_message(request, messages.SUCCESS, msg)
            url = reverse('main:admin_index')
            return redirect(url)

        else:
            return self.get(request, form)