from django.contrib.auth import get_user_model
from rest_framework import serializers

from api.models import Post


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'is_admin')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        queryset=get_user_model().objects.all(),
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Post
        fields = ('title', 'body', 'created_at', 'is_published', 'author')
