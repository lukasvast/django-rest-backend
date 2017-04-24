from .models import Author, Post
from .serializers import AuthorSerializer, PostSerializer
from rest_framework import generics
from rest_framework.authtoken.models import Token


#list all and create Author
class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


#retrieve by id, update or delete Author
class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


#retrieve by id Author
class AuthorName(generics.RetrieveUpdateAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'first_name'


#list all and create Posts
class PostList(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer


#retrieve by id, update and delete Post
class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer


#filter and list Posts by author.first_name
class PostAuthor(generics.ListAPIView):

    serializer_class = PostSerializer

    def get_queryset(self):

        author_first_name = self.kwargs['author_first_name']
        return Post.objects.filter(author__first_name=author_first_name)
