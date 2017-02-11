from django.conf.urls import url
from snippets import views

urlpatterns = [
    url(r'^incorrect/$', views.incorrect_list),
    url(r'^incorrect/(?P<pk>[0-9]+)/$', views.incorrect_detail),
    url(r'^correct/$', views.correct_list),
    url(r'^correct/(?P<pk>[0-9]+)/$', views.correct_detail),
]