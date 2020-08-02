from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from library.models import Book, Client
from library.serializers import (BookSerializer, ClientBookSerializer,
                                 ClientSerializer, UserSerializer)


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()

    def get_serializer_class(self):
        if self.action == 'books':
            return ClientBookSerializer
        return ClientSerializer

    @action(detail=True, methods=['GET'], name='Get Client Books')
    def books(self, request, *args, **kwargs):
        queryset = Client.objects.all().filter(pk = kwargs.get('pk'))

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    



