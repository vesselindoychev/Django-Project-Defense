from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

LETTERS_ERROR_MESSAGE = 'Value must contain only letters!'
CAR_MODEL_ERROR_MESSAGE = f'Model must contain only letters and digits'


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError(LETTERS_ERROR_MESSAGE)
    # if not value.isalpha():


def validate_car_model(value):
    for ch in value:
        if not ch.isalpha() and not ch.isdigit() and ch != ' ' and ch != '.':
            raise ValidationError(CAR_MODEL_ERROR_MESSAGE)


@deconstructible
class MaxImageSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.max_size * 1024 * 1024:
            raise ValidationError(f'Max file size is {self.max_size:.2f} MB')
