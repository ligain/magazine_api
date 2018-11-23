from django.contrib import admin
from django.contrib.auth import get_user_model

from api.models import Post


@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
