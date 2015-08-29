from django.conf.urls import patterns, url

from main import views

from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'gitmark.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.AdminIndexView.as_view(), name='admin_index'),
    url(r'^enterprise/$', views.EnterpriseView.as_view(), name='enterprise'),
    url(r'^home/$', views.HomeView.as_view(), name='home'),
]

# admin urls
urlpatterns += [    
    url(r'^repos/import/$', views.ImportRepoView.as_view(), name='admin_import_repo'),
    url(r'^repos/starred/$', views.StarredRepoView.as_view(), name='admin_starred_repo'),
    url(r'^collections/$', views.MyCollectionView.as_view(), name='my_collections'),
    url(r'^collections/(?P<pk>[0-9]+)/$', views.MyCollectionDetailView.as_view(), name='my_collection'),
]


