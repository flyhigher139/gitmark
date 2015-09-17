from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from . import models

class AccountResource(resources.ModelResource):

    class Meta:
        model = models.Account

class SocialInfoResource(resources.ModelResource):

    class Meta:
        model = models.SocialInfo

class AccountAdmin(ImportExportModelAdmin):
    resource_class = AccountResource

class SocialInfoAdmin(ImportExportModelAdmin):
    resource_class = SocialInfoResource

admin.site.register(models.Account, AccountAdmin)
admin.site.register(models.SocialInfo, SocialInfoAdmin)

