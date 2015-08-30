from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=256)
    def __unicode__(self):
        return self.name

class Repo(models.Model):
    name = models.CharField(max_length=256)
    full_name = models.CharField(max_length=256, unique=True)
    link = models.URLField()

    author = models.CharField(max_length=256)
    author_link = models.URLField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    language = models.ForeignKey(Language, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    starred_users = models.ManyToManyField(User)

   

    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=256)
    repos = models.ManyToManyField(Repo)
    counts = models.IntegerField(default=0)


class Collection(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User)
    repos = models.ManyToManyField(Repo, blank=True)
    last_update = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return self.user.username + '->' + self.name

class UserAction(models.Model):
    user = models.ForeignKey(User)
    repo = models.ForeignKey(Repo)
    action = models.CharField(max_length=256)



class RepoStarred(models.Model):
    repo = models.ForeignKey(Repo)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.user.username + ' -> ' + self.repo.full_name
