from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from registration.accounts.models import Profile
from registration.main.models import Vehicle, Make, CarModel, Advert

UserModel = get_user_model()


class ShowDetailsAdvertDetailViewTest(TestCase):
    VALID_USER_DATA = {
        'email': 'test124@gmail.com',
        'password': 'testuser1234',
    }

    VALID_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'User',
        'picture': 'mediafiles/profiles/person.png',
    }

    VALID_VEHICLE_DATA = {
        'price': 2000,
        'engine': Vehicle.DIESEL,
        'gearbox': Vehicle.AUTOMATIC_TRANSMISSION,
        'manufacture_date': 2003,
        'euro_standard': Vehicle.EURO5,
        'power': 230,
        'type': Vehicle.SEDAN,
        'mileage': 320123,
        'color': 'Black',
        'condition': Vehicle.USED,
        'location': Vehicle.PLOVDIV,

    }

    VALID_ADVERT_DATA = {
        'image': 'test-image.png',
        'date_of_publication': date.today(),
    }

    def __create_user(self, **credentials):
        return UserModel.objects.create_user(**credentials)

    def __create_make_and_model(self):
        car_make = Make.objects.create(name='Audi', )
        car_model = CarModel.objects.create(make=car_make, name='A6')

        return car_make, car_model

    def __create_valid_user_and_profile(self):
        user = self.__create_user(**self.VALID_USER_DATA)
        profile = Profile.objects.create(**self.VALID_PROFILE_DATA, user=user)

        return user, profile

    def test_when_opening_not_existing_profile__expect_404(self):
        response = self.client.get(reverse('show adverts', kwargs={'pk': 11}))
        self.assertEqual(404, response.status_code)

    def test_get__expect_correct_template(self):
        user, profile = self.__create_valid_user_and_profile()
        self.client.get(reverse('show adverts', kwargs={'pk': profile.pk}))
        self.assertTemplateUsed('main/show-adverts.html')

    def test_when_user_has_adverts__expect_to_return_only_users_adverts(self):
        user, profile = self.__create_valid_user_and_profile()

        credentials = {
            'email': 'testuser123@yahoo.com',
            'password': 'testuser123pass',
        }

        user2 = self.__create_user(**credentials)

        make, model = self.__create_make_and_model()
        car = Vehicle.objects.create(**self.VALID_VEHICLE_DATA, make=make, model=model, user=user,)
        advert = Advert.objects.create(**self.VALID_ADVERT_DATA, car=car, user=user, )
        # Advert.objects.create(**self.VALID_ADVERT_DATA, car=car, user=user2, )

        response = self.client.get(reverse('show adverts', kwargs={'pk': profile.pk}))

        self.assertEqual(
            [advert],
            response.context['adverts']
        )

    def test_when_user_has_not_vehicles__expect_to_return_empty_list_of_adverts(self):
        user, profile = self.__create_valid_user_and_profile()
        response = self.client.get(reverse('show adverts', kwargs={'pk': profile.pk}))

        self.assertEqual(
            [],
            response.context['adverts']
        )