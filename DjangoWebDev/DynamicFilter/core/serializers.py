from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.name")
    genre = serializers.CharField(source="get_genre_display")
    
    class Meta:
        model = Book
        fields = (
            'title',
            'author_name',
            'price',
            'genre',
        )
