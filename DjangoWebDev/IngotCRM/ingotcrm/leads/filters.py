from django import forms
from django.db.models import Q
import django_filters

from .models import Document


class DocumentFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        label='Title, lead or filename contains',
        lookup_expr='icontains',
        method='custom_filter',
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )

    data_added = django_filters.DateTimeFilter(
        field_name='date_added',
        lookup_expr='lte',
        widget=forms.DateTimeInput(
            attrs={'type': 'date', 'class': 'form-control'}
            )
        )
    
    is_secret = django_filters.BooleanFilter(
        widget=forms.CheckboxInput()
        )
    
    def custom_filter(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) |
            Q(lead__email__icontains=value) | 
            Q(lead__last_name__icontains=value) | 
            Q(lead__first_name__icontains=value)
        )
    
    class Meta:
        model = Document
        fields = ['title', 'is_secret']
    