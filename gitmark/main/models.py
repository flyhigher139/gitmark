from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class GitMarkMeta(models.Model):
    key = models.CharField(max_length=256)
    value = models.CharField(max_length=256, null=True, blank=True)
    flag = models.BooleanField(default=False)
    misc = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.key

@python_2_unicode_compatible
class Language(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Repo(models.Model):
    name = models.CharField(max_length=128)
    full_name = models.CharField(max_length=128, unique=True)
    link = models.URLField()

    author = models.CharField(max_length=128)
    author_link = models.URLField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    language = models.ForeignKey(Language, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    starred_users = models.ManyToManyField(User, blank=True) 

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=128)
    repos = models.ManyToManyField(Repo, blank=True)
    counts = models.IntegerField(default=0)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Collection(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User)
    repos = models.ManyToManyField(Repo, blank=True)
    last_update = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_date']

    def __str__(self):
        return self.user.username + '->' + self.name

# class UserAction(models.Model):
#     user = models.ForeignKey(User)
#     repo = models.ForeignKey(Repo)
#     action = models.CharField(max_length=128)



# class RepoStarred(models.Model):
#     repo = models.ForeignKey(Repo)
#     user = models.ForeignKey(User)

#     def __unicode__(self):
#         return self.user.username + ' -> ' + self.repo.full_name
