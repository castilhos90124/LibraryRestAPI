from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from bravosulBackEndChallenge.viewsets import UserViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'client', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
]
