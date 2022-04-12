from django import forms
from django.contrib.auth import get_user_model

from registration.main.models import Advert, PublishedAdvert


class CreateAdvertForm(forms.ModelForm):
    class Meta:
        model = Advert
        exclude = ('user',)


class EditAdvertForm(forms.ModelForm):
    class Meta:
        model = Advert
        exclude = ('user',)


class DeleteAdvertForm(forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Advert
        fields = ()


class CreatePublishAdvertForm(forms.ModelForm):
    class Meta:
        model = PublishedAdvert
        fields = ('advert',)
