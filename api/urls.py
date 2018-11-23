from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views

app_name = 'api'

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('users/<int:pk>/', views.UserView.as_view()),
    path('posts/', views.PostView.as_view()),
    path('posts/search/', views.PostSearchView.as_view()),
]