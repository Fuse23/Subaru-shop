from rest_framework.generics import ListAPIView
from .seriallizers import CategorySerializers
from cars.models import Cars, Category


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()


class CarsListAPIView(ListAPIView):
    serializer_class = CategorySerializers
    queryset = Cars.objects.all()
