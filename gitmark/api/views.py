from django.shortcuts import render
from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from api import serializers
from main import models


# Create your views here.
class RepoListTest(APIView):
  def get(self, request, format=None, *args, **kwargs):
    # return HttpResponse(kwargs['pk'])
    # return HttpResponse(request.user)
    quertset = models.Repo.objects.all()
    serializer = serializers.RepoSerializer(quertset, many=True)
    return Response(serializer.data)

class RepoList(generics.ListCreateAPIView):
  queryset = models.Repo.objects.all()
  serializer_class = serializers.RepoSerializer

class RepoDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = models.Repo.objects.all()
  serializer_class = serializers.RepoSerializer
