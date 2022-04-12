from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from registration.accounts.views import UserRegistrationView, UserLoginView, UserLogoutView, ChangeUserPassword, \
    UserDetailsView, UserEditView, UserDeleteView

urlpatterns = (
    # User

    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('user-details/<int:pk>/', UserDetailsView.as_view(), name='user details'),
    path('edit/user/<int:pk>/', UserEditView.as_view(), name='user edit'),
    path('delete/user/<int:pk>/', UserDeleteView.as_view(), name='user delete'),
    # User Password
    path('edit-password/', ChangeUserPassword.as_view(), name='edit password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('index')), name='password_change_done'),

)
