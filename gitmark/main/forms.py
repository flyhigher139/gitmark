#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

class CollectionForm(forms.Form):
	name = forms.CharField(max_length=256)
	description = forms.CharField(required=False, widget=forms.Textarea())