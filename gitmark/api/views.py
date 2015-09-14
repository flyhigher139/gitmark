from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseForbidden

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from main import models 
from . import serializers

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
