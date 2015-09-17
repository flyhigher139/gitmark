from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from main import models


class RepoResource(resources.ModelResource):

    class Meta:
        model = models.Repo

class LanguageResource(resources.ModelResource):

    class Meta:
        model = models.Language

class TagResource(resources.ModelResource):

    class Meta:
        model = models.Tag

class CollectionResource(resources.ModelResource):

    class Meta:
        model = models.Collection

class GitMarkMetaResource(resources.ModelResource):

    class Meta:
        model = models.GitMarkMeta



class RepoAdmin(ImportExportModelAdmin):
    resource_class = RepoResource

class LanguageAdmin(ImportExportModelAdmin):
    resource_class = LanguageResource

class TagAdmin(ImportExportModelAdmin):
    resource_class = TagResource

class CollectionAdmin(ImportExportModelAdmin):
    resource_class = CollectionResource

class GitMarkMetaAdmin(ImportExportModelAdmin):
    resource_class = GitMarkMetaResource


admin.site.register(models.Repo, RepoAdmin)
admin.site.register(models.Language, LanguageAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Collection, CollectionAdmin)
admin.site.register(models.GitMarkMeta, GitMarkMetaAdmin)
