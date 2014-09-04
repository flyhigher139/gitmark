from rest_framework import serializers
from main import models

class RepoSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Repo

class TagSerializer(serializers.ModelSerializer):
	# repo = RepoSerializer(many=True)
	class Meta:
		model = models.Tag
