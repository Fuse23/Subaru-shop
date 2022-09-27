from rest_framework import serializers
from cars.models import Cars, Category


class CategorySerializers(serializers.ModelSerializer):
    title = serializers.CharField(required=True)

    class Meta:
        model = Category
        fields = [
            'id', 'title'
        ]


class CarsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Cars
        fields = [
            'id', 'title'
        ]

