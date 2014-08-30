from django.conf.urls import patterns, include, url

from api import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gitmark.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^$', views.EnterpriseView.as_view(), name='home')
)
