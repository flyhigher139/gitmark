from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Repo(models.Model):
	name=models.CharField(max_length=200)
	link=models.URLField()
	starred=models.IntegerField(blank=True)
	fork=models.IntegerField(blank=True)
	author=models.CharField(max_length=200)
	author_link=models.URLField()
	language=models.CharField(max_length=200)
	subject=models.CharField(max_length=200)
	last_update=models.DateTimeField(auto_now=True)

class RepoCreation(models.Model):
	user=models.ForeignKey(User)
	repo=models.ForeignKey(Repo)

class Tag(models.Model):
	name=models.CharField(max_length=200)
	repos=models.ManyToManyField(Repo)

class Collection(models.Model):
	name=models.CharField(max_length=200)
	user=models.ForeignKey(User)
	repos=models.ManyToManyField(Repo)
	last_update=models.DateTimeField(auto_now=True)



		
		