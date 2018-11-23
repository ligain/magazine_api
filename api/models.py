from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from magazine.managers import UserManager
from api.helpers import get_stub_user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        return self.is_admin

    @property
    def is_editor(self):
        """
        Is the user an editor who
        can do anything with posts?
        """
        return self.groups.filter(name='Editors').exists()

    @property
    def is_journalist(self):
        """
        Is the user an journalist who can:
        - edit its own posts
        - add new posts
        """
        return self.groups.filter(name='Journalists').exists()

    def __str__(self):
        return f'User <{self.email}>'


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.SET(get_stub_user),
                               related_name='posts')
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'Post <{self.title[:50]}>'
