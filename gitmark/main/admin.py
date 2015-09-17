from django.contrib import admin
from main import models

# Register your models here.
admin.site.register(models.Repo)
admin.site.register(models.Language)
admin.site.register(models.Tag)
admin.site.register(models.Collection)
admin.site.register(models.GitMarkMeta)
