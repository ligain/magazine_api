from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

app_name = 'api'

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]