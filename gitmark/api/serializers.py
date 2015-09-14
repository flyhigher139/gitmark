#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User

from rest_framework import serializers

from main import models
from accounts import models as account_models

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'password')
		extra_kwargs = {'password': {'write_only': True}}