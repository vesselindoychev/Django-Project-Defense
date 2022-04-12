from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms
from registration.accounts.models import Profile

UserModel = get_user_model()


class CreateUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email',)

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            user=user,
        )

        if commit:
            profile.save()
        return user


class EditUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

        BIRTDAY_YEARS = [i for i in range(1980, 2023)]
        widgets = {
            'date_of_birth': forms.SelectDateWidget(
                years=BIRTDAY_YEARS,
            ),
            'description': forms.Textarea(
                attrs={
                    'rows': 4,
                }
            )
        }


class DeleteUserForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()
