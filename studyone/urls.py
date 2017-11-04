from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from studyone import views
from studyone import views_users

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    url(r'^api/adduser', views_users.adduser, name='adduser'),
    url(r'^api/userlist', views_users.userlist, name='userlist'),
    url(r'^api/deleteuser', views_users.deleteuser, name='deleteuser')
]

urlpatterns = format_suffix_patterns(urlpatterns)