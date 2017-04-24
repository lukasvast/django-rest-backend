from django.contrib.auth.models import User, Group
from .models import Author, Post
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


#serialize data from Author model
#allows to CRUD Author
class AuthorSerializer(serializers.HyperlinkedModelSerializer):

    posts = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='post-detail'
    )

    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'email', 'posts')


#serialize data from Post model
#allows to CRUD Post(nested relationship)
class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        many=False,
        queryset=Author.objects.all(),
        view_name='author-detail'
    )

    class Meta:
        model = Post
        fields = ('id', 'post_text', 'pub_date', 'author')
