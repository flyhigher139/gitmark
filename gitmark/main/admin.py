from django.contrib import admin
import models

# Register your models here.
admin.site.register(models.Repo)
admin.site.register(models.RepoCreation)
admin.site.register(models.Tag)
admin.site.register(models.Collection)