from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=256)
    def __unicode__(self):
        return self.name

class Repo(models.Model):
    name = models.CharField(max_length=256)
    link = models.URLField()
    # starred = models.IntegerField(blank=True, null=True)
    # fork = models.IntegerField(blank=True)
    author = models.CharField(max_length=256)
    author_link = models.URLField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    language = models.ForeignKey(Language, blank=True, null=True)
    # subject = models.CharField(max_length=256)
    # last_update = models.DateTimeField(auto_now=True)
    # creator = models.ForeignKey(User)
    # blocked = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name
#
# # class RepoCreation(models.Model):
# #     user=models.ForeignKey(User)
# #     repo=models.ForeignKey(Repo)
#
class Tag(models.Model):
    name = models.CharField(max_length=256)
    repos = models.ManyToManyField(Repo)
    counts = models.IntegerField(default=0)

# class TagStatistic(models.Model):
#     tag = models.ForeignKey(Tag)
#     repo_count = models.IntegerField(default=0)

class Collection(models.Model):
    name = models.CharField(max_length=256)
    user = models.ForeignKey(User)
    repos = models.ManyToManyField(Repo)
    last_update = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

class UserAction(models.Model):
    user = models.ForeignKey(User)
    repo = models.ForeignKey(Repo)
    action = models.CharField(max_length=256)

# class Account(models.Model):
#   user = models.ForeignKey(User, related_name="Account_User")
#   avatar = models.URLField(null=True, blank=True)
#   repos_starred = models.ForeignKey(Repo, related_name="Account_Repo")
#   following = models.ManyToManyField(User, blank=True, null=True)

class RepoStarred(models.Model):
    repo = models.ForeignKey(Repo)
    user = models.ForeignKey(User)
