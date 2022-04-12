import datetime
from datetime import date

from django import forms

from registration.main.models import Vehicle, CarModel


class CreateVehicleForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self.fields['model'].queryset = CarModel.objects.none()

        if 'make' in self.data:
            try:
                make_id = int(self.data.get('make'))
                self.fields['model'].queryset = CarModel.objects.filter(make_id=make_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['model'].queryset = self.instance.make.model_set.order_by('name')

    def save(self, commit=True):
        vehicle = super().save(commit=False)
        vehicle.user = self.user
        if commit:
            vehicle.save()
        return vehicle

    class Meta:
        model = Vehicle
        fields = ('make', 'model', 'additional_info', 'price', 'engine', 'gearbox', 'manufacture_date',
                   'euro_standard', 'power', 'type', 'mileage', 'color', 'technical_characteristic',
                   'condition', 'location',)
        labels = {
            'manufacture_date': 'Manufacture Date',
            'technical_characteristic': 'Technical Characteristics',
            'additional_info': 'Additional Info'
        }

        widgets = {

            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'e.g 3200 BGN',
                },
            ),
            'power': forms.NumberInput(
                attrs={
                    'placeholder': 'e.g 112hp',
                },
            ),

            'mileage': forms.NumberInput(
                attrs={
                    'placeholder': 'e.g 200000 km',
                },
            ),

            'technical_characteristic': forms.URLInput(
                attrs={
                    'placeholder': 'URL Field',
                },
            ),
        }


class EditVehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('make', 'model', 'additional_info', 'price', 'engine', 'gearbox', 'manufacture_date',
                  'euro_standard', 'power', 'type', 'mileage', 'color', 'technical_characteristic',
                  'condition', 'location',)
        labels = {
            'manufacture_date': 'Manufacture Date',
            'technical_characteristic': 'Technical Characteristics',
            'additional_info': 'Additional Info'
        }


class DeleteVehicleForm(forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Vehicle
        fields = ()
