from django.conf.urls import patterns, include, url

from main import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gitmark.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^enterprise$', views.EnterpriseView.as_view(), name='enterprise'),
    url(r'^home$', views.HomeView.as_view(), name='home'),
    url(r'^$', views.AdminIndexView.as_view(), name='admin_index'),
    url(r'^repos/import', views.ImportRepoView.as_view(), name='admin_import_repo'),
    url(r'^repos/starred', views.StarredRepoView.as_view(), name='admin_starred_repo'),
)
