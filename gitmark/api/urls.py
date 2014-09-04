from django.conf.urls import patterns, include, url
from api import views

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gitmark.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^$', views.EnterpriseView.as_view(), name='home')
    url(r'^repos/$', views.RepoList.as_view(), name='repos'),
    url(r'^repo/(?P<pk>[0-9]+)/$', views.RepoDetail.as_view(), name='repo_detail'),
    url(r'^repos/(?P<pk>[0-9]+)/$', views.RepoListTest.as_view(), name='repos'),
)
