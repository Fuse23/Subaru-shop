from django.urls import path
from api.api_views import CategoryListAPIView, CarsListAPIView


urlpatterns = [
    path('category/', CategoryListAPIView.as_view()),
    path('cars/', CarsListAPIView.as_view())
]
