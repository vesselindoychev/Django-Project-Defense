from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models

from registration.accounts.managers import RegistrationUserManager
from registration.common.validators import validate_only_letters, MaxImageSizeInMbValidator


class RegistrationUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    # Here you choose what you want to authenticate the user with
    # email or username

    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = RegistrationUserManager()


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 20
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 20
    LAST_NAME_MIN_LENGTH = 2
    IMAGE_MAX_SIZE_IN_MB = 5
    UPLOAD_TO_DIR = 'profiles/'

    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'

    GENDERS = (
        MALE,
        FEMALE,
        OTHER,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        ),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        ),
    )

    picture = models.ImageField(
        upload_to=UPLOAD_TO_DIR,
        validators=(
            MaxImageSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        ),

    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max(len(g) for g in GENDERS),
        choices=((g, g) for g in GENDERS),
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        RegistrationUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

