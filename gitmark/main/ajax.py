import json

from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.db.models import Count, Q
from django.conf import settings

from accounts import github_auth
from . import models, forms, tasks

def change_star_status(request, pk):
    try:
        repo = models.Repo.objects.get(pk=pk)
    except models.Repo.DoesNotExist:
        raise Http404

    if request.user in repo.starred_users.all():
        repo.starred_users.remove(request.user)
    else:
        repo.starred_users.add(request.user)

    return HttpResponse('succeed')

def list_user_collections(request):
    collections = models.Collection.objects.filter(user=request.user)
    collection_list = []
    for collection in collections:
        obj = {
            'id':collection.id,
            'name': collection.name,
        }
        collection_list.append(obj)

    return HttpResponse(json.dumps(collection_list))

def repo_collection_status(request, repo_id):
    repo_id = int(repo_id)
    try:
        repo = models.Repo.objects.get(pk=repo_id)
    except models.Repo.DoesNotExist:
        raise Http404

    collections = models.Collection.objects.filter(user=request.user)
    collection_list = []
    for collection in collections:
        obj = {
            'id':collection.id,
            'name': collection.name,
            'selected': repo in collection.repos.all()
        }
        collection_list.append(obj)

    return HttpResponse(json.dumps(collection_list))
