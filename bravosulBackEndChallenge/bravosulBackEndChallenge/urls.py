from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from library.views import UserViewSet, BookViewSet, ClientViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'books', BookViewSet)
router.register(r'client', ClientViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
]
