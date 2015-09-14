from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from main import models 
from . import serializers, spec

# Create your views here.

class StargazersListView(APIView):
    def get(self, request, pk):
        pk = int(pk)
        try:
            repo = models.Repo.objects.get(pk=pk)
        except models.Repo.DoesNotExist:
            raise Http404

        users = repo.starred_users
        
        serializer = serializers.UserSerializer(users, many=True)

        return Response(serializer.data)

class UserStarredRepos(generics.ListAPIView):
    queryset = models.Repo.objects.all()
    serializer_class = serializers.RepoSerializer
    pagination_class = spec.StandardResultsSetPagination

    def get_queryset(self, request, pk=0):
        if pk == 0:
            user = request.user
        else:
            pk = int(pk)
            try:
                user = User.objects.get(pk=pk)
            except User.DoesNotExist:
                raise Http404

        repos = models.Repo.objects.filter(starred_users=user)
        return repos

    def list(self, request, pk=0):
        queryset = self.get_queryset(request, pk)

        serializer = serializers.RepoSerializer(queryset, many=True)

        return Response(serializer.data)
