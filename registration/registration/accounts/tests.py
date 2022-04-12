from datetime import date

from django.contrib.auth import get_user_model
from django.db.models import Model
from django.test import TestCase
from django.urls import reverse

from registration.accounts.models import Profile
from registration.main.models import Vehicle, Make, CarModel, Advert, PublishedAdvert

UserModel = get_user_model()


class UserDetailsViewTest(TestCase):
    USER_VALID_DATA = {
        'email': 'test123@gmail.com',
        'password': 'test123',
    }

    PROFILE_VALID_DATA = {
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
        'image': 'asd.png',
        'date_of_publication': date.today(),
    }

    def __create_user(self, **credentials):
        return UserModel.objects.create_user(**credentials)

    def __create_make_and_model(self):
        car_make = Make.objects.create(name='Audi', )
        car_model = CarModel.objects.create(make=car_make, name='A6')

        return car_make, car_model

    def __create_valid_user_and_profile(self):
        user = self.__create_user(**self.USER_VALID_DATA)

        profile = Profile.objects.create(
            **self.PROFILE_VALID_DATA,
            user=user,
        )

        return user, profile

    def test_when_opening_not_existing_profile__expect_404(self):
        response = self.client.get(reverse('user details', kwargs={'pk': 1, }))
        self.assertEqual(404, response.status_code)

    def test_get__expect_correct_template(self):
        user, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.USER_VALID_DATA)
        self.client.get(reverse('user details', kwargs={'pk': profile.pk}))
        self.assertTemplateUsed('accounts/user-details.html')

    def test_when_user_is_owner__expect_is_owner_to_be_true(self):
        user, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.USER_VALID_DATA)

        response = self.client.get(reverse('user details', kwargs={'pk': profile.pk}))
        self.assertTrue(response.context['is_owner'])

    def test_when_user_is_not_owner__expect_is_owner_to_be_false(self):
        user, profile = self.__create_valid_user_and_profile()
        credentials = {
            'email': 'testmail123@gmail.com',
            'password': 'testuser123asd',
        }

        self.__create_user(**credentials)
        self.client.login(**credentials)

        response = self.client.get(reverse('user details', kwargs={'pk': profile.pk}))
        self.assertFalse(response.context['is_owner'])

    def test_when_no_published_adverts__expect_published_adverts_count_to_be_zero(self):
        user, profile = self.__create_valid_user_and_profile()
        make, model = self.__create_make_and_model()
        car = Vehicle.objects.create(**self.VALID_VEHICLE_DATA, make=make, model=model, user=user, )

        response = self.client.get(reverse('user details', kwargs={'pk': profile.pk}))

        self.assertEqual(0, response.context['total_adverts_count'])

    def test_when_published_adverts__expect_published_adverts_count_to_be_correct(self):
        user, profile = self.__create_valid_user_and_profile()
        make, model = self.__create_make_and_model()
        car = Vehicle.objects.create(**self.VALID_VEHICLE_DATA, make=make, model=model, user=user, )
        advert = Advert.objects.create(**self.VALID_ADVERT_DATA, car=car, user=user,)
        published_advert = PublishedAdvert.objects.create(advert=advert, user=user)
        response = self.client.get(reverse('user details', kwargs={'pk': profile.pk}))

        self.assertEqual(1, response.context['total_adverts_count'])
