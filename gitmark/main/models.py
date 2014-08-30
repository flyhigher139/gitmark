from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Language(models.Model):
	name = models.CharField(max_length=256)

class Repo(models.Model):
	name=models.CharField(max_length=256)
	link=models.URLField()
	starred=models.IntegerField(blank=True, null=True)
	fork=models.IntegerField(blank=True)
	author=models.CharField(max_length=256)
	author_link=models.URLField(blank=True, null=True)
	language=models.ForeignKey(Language)
	subject=models.CharField(max_length=256)
	last_update=models.DateTimeField(auto_now=True)
	editor = models.ForeignKey(User)

# class RepoCreation(models.Model):
# 	user=models.ForeignKey(User)
# 	repo=models.ForeignKey(Repo)

class Tag(models.Model):
	name=models.CharField(max_length=256)
	repos=models.ManyToManyField(Repo, blank=True, null=True)

class TagStatistic(models.Model):
	tag = models.ForeignKey(Tag)
	repo_count = models.IntegerField(default=0)

class Collection(models.Model):
	name=models.CharField(max_length=256)
	user=models.ForeignKey(User)
	repos=models.ManyToManyField(Repo)
	last_update=models.DateTimeField(auto_now=True)

# class Account(models.Model):
# 	user = models.OneToOneField(User)
# 	repos = models.



		
		