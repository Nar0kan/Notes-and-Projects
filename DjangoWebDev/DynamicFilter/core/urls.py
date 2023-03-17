from django.urls import path
from .views import staticFilterView, dynamicFilterListView, landingView, BookListAPIView

app_name = "core"

urlpatterns = [
    path('', landingView, name="landing"),
    path('static_form/', staticFilterView, name="static-filter"),
    path('dynamic_form/', dynamicFilterListView.as_view(), name="dynamic-filter"),
    path('api/', BookListAPIView.as_view(), name="api-filter"),
]
