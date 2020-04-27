from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'game', views.GameViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls)),
    ]
