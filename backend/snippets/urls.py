from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'^db/$', views.db_list),
    url(r'^db/(?P<pk>-?[0-9]+)/$', views.db_detail),
    url(r'^db/(?P<db>[A-Za-z0-9_-]+)/(?P<ct>incorrect|correct)/$', views.url_list),
    url(r'^db/(?P<db>[A-Za-z0-9_-]+)/(?P<ct>incorrect|correct)/(?P<page>-?[0-9]+)/$', views.url_list_by_page),
    url(r'^db/(?P<db>[A-Za-z0-9_-]+)/(?P<ct>incorrect|correct)/(?P<page>-?[0-9]+)/(?P<rows>[0-9]+)/$', views.url_list_by_page),
]