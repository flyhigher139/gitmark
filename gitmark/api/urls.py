from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    # url(r'^$', main_view.AdminIndexView.as_view()),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^main/', include('main.urls', namespace='main')),
    # url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^repos/(?P<pk>[0-9]+)/stargazers/$', views.StargazersListView.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/starred/$', views.UserStarredRepos.as_view()),
    url(r'^user/starred/$', views.UserStarredRepos.as_view()),
    url(r'^user/starred/(?P<pk>[0-9]+)/$', views.StarActivityView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)