from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class Language(models.Model):
	name = models.CharField(max_length=256)
	is_popular = models.BooleanField(default=False)
	def __unicode__(self):
		return self.name

class Repo(models.Model):
	name = models.CharField(max_length=256)
	link = models.URLField()
	# starred = models.IntegerField(blank=True, null=True)
	# fork = models.IntegerField(blank=True)
	author = models.CharField(max_length=256)
	author_link = models.URLField(blank=True, null=True)
	language = models.CharField(max_length=256)
	desc = models.TextField()
	# last_update = models.DateTimeField(auto_now=True)
	# creator = models.ForeignKey(User)
	tags = models.ManyToManyField(Tag, blank=True, null=True)
	blocked = models.BooleanField(default=False) #administrator use this filed for repo management

	def __unicode__(self):
		return self.name
#
# # class RepoCreation(models.Model):
# # 	user=models.ForeignKey(User)
# # 	repo=models.ForeignKey(Repo)
#
class Tag(models.Model):
	name = models.CharField(max_length=256)
	# counts = models.IntegerField(default=0)

# class TagStatistic(models.Model):
# 	tag = models.ForeignKey(Tag)
# 	repo_count = models.IntegerField(default=0)
