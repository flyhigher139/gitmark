from django.db import models
from django.contrib.auth.models import User

from main import models as main_models

# Create your models here.

class Account(models.Model):
	user = models.OneToOneField(User)
	avatar = models.URLField(null=True, blank=True)
	# repos_starred = models.ForeignKey(main_models.Repo, related_name="Account_Repo")
	# following = models.ManyToManyField(User, blank=True, null=True)

class UserRepos(models.Model):
    user = models.ForeignKey(User)
    repo = models.ForeignKey(main_models.Repo, related_name="Account_Repo")

class Collection(models.Model):
	name = models.CharField(max_length=256)
	user = models.ForeignKey(User)
	repos = models.ManyToManyField(main_models.Repo)
	last_update = models.DateTimeField(auto_now=True)

# class UserAction(models.Model):
# 	user = models.ForeignKey(User)
# 	repo = models.ForeignKey(Repo)
# 	action = models.CharField(max_length=256)
