from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import viewsets

from library.serializers import UserSerializer, BookSerializer, ClientSerializer
from library.models import Book, Client



# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer