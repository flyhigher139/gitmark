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
    starred_users = models.ManyToManyField(User)

    # def save(self, *args, **kwargs):
    #     try:
    #         repo = Repo.objects.get(full_name=self.full_name)
    #         return repo
    #     except Repo.DoesNotExist:
    #         return super(Repo, self).save(*args, **kwargs)

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
    description = models.TextField(blank=True)
    user = models.ForeignKey(User)
    repos = models.ManyToManyField(Repo, blank=True)
    last_update = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + '->' + self.name

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

    def __unicode__(self):
        return self.user.username + ' -> ' + self.repo.full_name
