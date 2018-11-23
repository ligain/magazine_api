from django.db.models import Q
from rest_framework import generics
from django.contrib.auth import get_user_model

from api.forms import QueryForm
from api.models import Post
from api.serializers import UserSerializer, PostSerializer


class UserView(generics.RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class PostView(generics.ListCreateAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            queryset = Post.objects.filter(is_published=True)
        elif user.is_editor or user.is_admin:
            queryset = Post.objects.all()
        elif user.is_journalist:
            queryset = Post.objects.filter(author=user)
        else:
            queryset = Post.objects.filter(is_published=True)
        return queryset


class PostSearchView(generics.ListAPIView):
    serializer_class = PostSerializer
    query_lookup = 'q'

    def get_queryset(self):
        query = self.request.query_params.get(self.query_lookup, '')
        query_form = QueryForm({self.query_lookup: query})
        if query_form.is_valid():
            queryset = Post.objects.filter(
                Q(
                    Q(title__icontains=query_form.cleaned_data[self.query_lookup]) |
                    Q(body__icontains=query_form.cleaned_data[self.query_lookup])
                ),
                is_published=True
            )
        else:
            queryset = Post.objects.none()
        return queryset
