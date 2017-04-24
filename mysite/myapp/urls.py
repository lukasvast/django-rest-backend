from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import restviews
from rest_framework.authtoken import views


urlpatterns = [
    url(r'^authors/$', restviews.AuthorList.as_view(), name='author-list'),
    url(r'^authors/(?P<pk>[0-9]+)/$', restviews.AuthorDetail.as_view(), name='author-detail'),
    url(r'^authorsByName/(?P<first_name>[\w.@+-]+)/$', restviews.AuthorName.as_view(), name='author-name'),

    url(r'^posts/$', restviews.PostList.as_view(), name='post-list'),
    url(r'^posts/(?P<pk>[0-9]+)/$', restviews.PostDetail.as_view(), name='post-detail'),
    url(r'^postsAuthor/(?P<author_first_name>[\w.@+-]+)/$', restviews.PostAuthor.as_view(), name='post-author'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #return token providing username and password POST
    url(r'^api-token-auth/', views.obtain_auth_token),
]

urlpatterns = format_suffix_patterns(urlpatterns)
