import django_filters
from core.models import Book


class BookFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()
    class Meta:
        model = Book
        fields = {
            'title': ['icontains'],
            'author__name': ['icontains'],
            'genre': ['exact'],
            }