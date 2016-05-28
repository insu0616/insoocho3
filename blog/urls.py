from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.detail, name="detail"),
    url(r'^createpost/$', views.post_new, name="post-create"),
    url(r'^(?P<pk>\d+)/createcomment$', views.comment_new, name="comment-create"),
]



