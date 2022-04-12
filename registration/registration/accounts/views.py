from django import forms
from django.contrib import messages
from django.contrib.auth import forms as auth_forms, get_user_model, login
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render, redirect

from registration.accounts.forms import EditUserForm, DeleteUserForm, CreateUserForm
from registration.accounts.models import Profile
from registration.main.models import Advert, Vehicle, PublishedAdvert

UserModel = get_user_model()


# class UserRegistrationForm(auth_forms.UserCreationForm):
#     class Meta:
#         model = UserModel
#         fields = ('email',)
#
#     def save(self, commit=True):
#         user = super().save(commit=commit)
#
#         profile = Profile(
#             user=user,
#         )
#
#         if commit:
#             profile.save()
#         return user


class UserRegistrationView(views.CreateView):
    form_class = CreateUserForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'

    def get_success_url(self):
        next = self.request.GET.get('next', None)
        if next:
            return next
        return reverse_lazy('index')


class UserLogoutView(auth_views.LogoutView):
    pass


class ChangeUserPassword(auth_views.PasswordChangeView):
    template_name = 'accounts/change-password.html'


class UserDetailsView(views.DetailView):
    model = Profile
    template_name = 'accounts/user-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        cars = Vehicle.objects.filter(user_id=self.object.user_id)
        adverts = PublishedAdvert.objects.filter(advert__car__in=cars).distinct()
        total_adverts_count = len(adverts)

        context.update({
            'total_adverts_count': total_adverts_count,
            'is_owner': self.object.user_id == self.request.user.id,
        })

        return context


class UserEditView(views.UpdateView):
    model = Profile
    form_class = EditUserForm
    template_name = 'accounts/user-edit.html'

    def get_success_url(self):
        return reverse_lazy('user details', kwargs={'pk': self.object.user_id})


class UserDeleteView(views.DeleteView):
    model = Profile
    form_class = DeleteUserForm
    template_name = 'accounts/user-delete.html'

    def get_success_url(self):
        return reverse_lazy('index')
