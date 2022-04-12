from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from registration.accounts.models import Profile
from registration.main.models import Vehicle, Make, CarModel, Advert, PublishedAdvert

UserModel = get_user_model()


class PublishAdvertCreateViewTest(TestCase):
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

    ADVERT_VALID_DATA = {
        'image': 'image-test.png',
        'date_of_publication': date.today(),
    }

    def __create_make_and_model(self):
        car_make = Make.objects.create(name='Audi')
        car_model = CarModel.objects.create(make=car_make, name='A6')

        return car_make, car_model

    def __create_valid_profile_and_user(self):
        user = UserModel.objects.create_user(**self.VALID_USER_DATA)
        profile = Profile.objects.create(**self.VALID_PROFILE_DATA, user=user)

        return user, profile

    def test_get__expect_correct_template(self):
        response = self.client.get(reverse('publish advert create'))
        self.assertTemplateUsed(response, 'main/published-advert-create.html')

    def test_publish_advert__when_all_is_valid__expect_to_be_publish_advert(self):
        user, profile = self.__create_valid_profile_and_user()
        make, model = self.__create_make_and_model()
        vehicle = Vehicle.objects.create(**self.VALID_VEHICLE_DATA, make=make, model=model, user=user, )
        advert = Advert.objects.create(**self.ADVERT_VALID_DATA, car=vehicle, user=user)
        published_advert = PublishedAdvert.objects.create(advert=advert, user=user)

        self.assertIsNotNone(published_advert)
        self.assertEqual(published_advert.user_id, user.id)

    def test_publish_advert__when_all_is_valid__expect_to_redirect_to_dashboard(self):
        user, profile = self.__create_valid_profile_and_user()
        make, model = self.__create_make_and_model()
        vehicle = Vehicle.objects.create(**self.VALID_VEHICLE_DATA, make=make, model=model, user=user, )
        advert = Advert.objects.create(**self.ADVERT_VALID_DATA, car=vehicle, user=user)
        published_advert = PublishedAdvert.objects.create(advert=advert, user=user)

        response = self.client.post(
            reverse('publish advert create'),
            data={published_advert.advert_id: advert.id,
                  published_advert.user_id: user.id,
                  }

        )

        expected_url = reverse('show dashboard')
        self.assertRedirects(response, expected_url)
        self.assertEqual(response.status_code, 302)
