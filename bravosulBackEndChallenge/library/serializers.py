from django.contrib.auth.models import User
from rest_framework import serializers

from library.models import Book, Client


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username','is_staff']

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    books = BookSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Client
        fields = '__all__'

class ClientBookSerializer(serializers.HyperlinkedModelSerializer):
    books = BookSerializer(many=True, required=False, read_only=True)

    class Meta:
        model = Client
        fields = ['books']

