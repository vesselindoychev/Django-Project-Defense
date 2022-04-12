from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from registration.accounts.models import Profile
from registration.main.models import Vehicle, Make, CarModel, Advert

UserModel = get_user_model()


class EditAdvertViewTest(TestCase):
    VALID_ADVERT_DATA = {
        'image': 'test-image.png',
        'date_of_publication': date.today(),
    }

    VALID_VEHICLE_DATA = {
        'price': 2000,
        'engine': Vehicle.DIESEL,
        'gearbox': Vehicle.MANUAL_TRANSMISSION,
        'manufacture_date': 2004,
        'euro_standard': Vehicle.EURO3,
        'power': 190,
        'type': Vehicle.SEDAN,
        'mileage': 130123,
        'color': 'Black',
        'condition': Vehicle.USED,
        'location': Vehicle.PLOVDIV,

    }

    VALID_USER_DATA = {
        'email': 'testuser123@yahoo.com',
        'password': 'testuser123pass',
    }

    VALID_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'User',
        'picture': 'test.png',
    }

    def __create_make_and_model(self):
        car_make = Make.objects.create(name='Audi')
        car_model = CarModel.objects.create(make=car_make, name='A6')

        return car_make, car_model

    def __create_valid_profile_and_user(self):
        user = UserModel.objects.create_user(**self.VALID_USER_DATA)
        profile = Profile.objects.create(**self.VALID_PROFILE_DATA, user=user)

        return user, profile

    def test_get__expect_to_return_correct_template(self):
        user, profile = self.__create_valid_profile_and_user()
        make, model = self.__create_make_and_model()
        car = Vehicle.objects.create(**self.VALID_VEHICLE_DATA, make=make, model=model, user=user)
        advert = Advert.objects.create(**self.VALID_ADVERT_DATA, car=car, user=user)

        response = self.client.get(reverse('edit advert', kwargs={'pk': advert.pk}))
        self.assertTemplateUsed(response, 'main/advert-edit.html')

    def test_update_advert__when_all_is_valid__expect_to_redirect_to_correct_url(self):
        user, profile = self.__create_valid_profile_and_user()
        make, model = self.__create_make_and_model()
        car = Vehicle.objects.create(**self.VALID_VEHICLE_DATA, make=make, model=model, user=user)
        advert = Advert.objects.create(**self.VALID_ADVERT_DATA, car=car, user=user)

        response = self.client.post(
            reverse('edit advert', kwargs={'pk': advert.pk}),
            data=self.VALID_ADVERT_DATA,
        )

        advert = Advert.objects.first()

        expected_url = reverse('show advert details', kwargs={'pk': advert.pk})
        self.assertRedirects(response, expected_url)
        self.assertEqual(302, response.status_code)
