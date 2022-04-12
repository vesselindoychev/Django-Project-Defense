import django_filters
from registration.main.models import Vehicle, PublishedAdvert, CarModel
from django import forms


class VehicleFilter(django_filters.FilterSet):
    class Meta:
        model = Vehicle
        fields = ('make', 'model', 'price', 'engine', 'gearbox', 'manufacture_date', 'euro_standard', 'power',
                  'type', 'mileage', 'color', 'condition', 'location')

        # exclude = ('user', 'technical_characteristic')


class PublishedAdvertFilter(django_filters.FilterSet):
    class Meta:
        model = PublishedAdvert
        exclude = ('user',)
