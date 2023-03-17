from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Journal, Category, Book
from .forms import BookNameFilterForm
from .filters import BookFilter
from .serializers import BookSerializer


class dynamicFilterListView(ListView):
    queryset = Book.objects.filter(number_in_stock__gt=0)
    template_name = 'dynamic_form.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = BookFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        return context


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = BookFilter


# def dynamicFilterView(request):
#     book_filter = BookFilter(request.GET, queryset=Book.objects.all())

#     context = {
#         'form': book_filter.form,
#         'books': book_filter.qs,
#     }
#     return render(request, "dynamic_form.html", context)


def landingView(request):
    return render(request, "landing.html", {})


def is_valid_quertparam(param):
    return param != '' and param is not None


def staticFilterView(request):
    # Initial querysets
    qs = Journal.objects.all()
    categories = Category.objects.all()

    # Search bars
    title_contains_query = request.GET.get("title_contains")
    title_exact_query = request.GET.get("title_exact")
    title_or_author_query = request.GET.get("title_or_author")

    # Filters
    view_count_min = request.GET.get("view_count_min")
    view_count_max = request.GET.get("view_count_max")
    date_min = request.GET.get("date_min")
    date_max = request.GET.get("date_max")
    category = request.GET.get("category")
    reviewed = request.GET.get("reviewed")
    not_reviewed = request.GET.get("not_reviewed")

    # Filtering
    if is_valid_quertparam(title_contains_query):
        qs = qs.filter(title__icontains=title_contains_query)
    elif is_valid_quertparam(title_exact_query):
        qs = qs.filter(title__iexact=title_exact_query)
    elif is_valid_quertparam(title_or_author_query):
        qs = qs.filter(Q(title__icontains=title_or_author_query) | Q(author__name__icontains=title_or_author_query)).distinct()

    if is_valid_quertparam(view_count_min):
        qs = qs.filter(views__gte=view_count_min)
    
    if is_valid_quertparam(view_count_max):
        qs = qs.filter(views__lt=view_count_max)
    
    if is_valid_quertparam(date_min):
        qs = qs.filter(publish_date__gte=date_min)
    
    if is_valid_quertparam(date_max):
        qs = qs.filter(publish_date__lt=date_max)
    
    if is_valid_quertparam(category) and category != "Choose...":
        qs = qs.filter(categories__name=category)
    
    if reviewed == "on":
        qs = qs.filter(reviewed=True)
    elif not_reviewed == "on":
        qs = qs.filter(reviewed=False)
    
    # Context
    context = {
        'queryset': qs,
        'categories': categories
    }
    
    return render(request, "static_form.html", context)
