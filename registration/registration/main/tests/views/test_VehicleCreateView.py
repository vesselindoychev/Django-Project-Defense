from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from registration.accounts.models import Profile
from registration.main.models import Vehicle, Make, CarModel

UserModel = get_user_model()


class VehicleCreateViewTest(TestCase):
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

    def test_get__expect_correct_template(self):
        response = self.client.get(reverse('create vehicle'))
        self.assertTemplateUsed(response, 'main/vehicle-create.html')

    def test_create_vehicle__when_all_is_valid__expect_to_return_users_vehicle(self):
        user, profile = self.__create_valid_profile_and_user()
        make, model = self.__create_make_and_model()
        car = Vehicle.objects.create(**self.VALID_VEHICLE_DATA, make=make, model=model, user=user, )

        self.client.post(
            reverse('create vehicle'),
            data=self.VALID_VEHICLE_DATA,
        )

        self.assertEqual(car.user_id, user.id)

    def test_create_vehicle__when_everything_is_valid__expect_to_create_vehicle(self):
        user, profile = self.__create_valid_profile_and_user()
        make, model = self.__create_make_and_model()
        Vehicle.objects.create(**self.VALID_VEHICLE_DATA, make=make, model=model, user=user, )

        self.client.post(
            reverse('create vehicle'),
            data=self.VALID_VEHICLE_DATA,
        )
        vehicle = Vehicle.objects.first()

        self.VALID_VEHICLE_DATA['make'] = make
        self.VALID_VEHICLE_DATA['model'] = model

        self.assertIsNotNone(vehicle)
        self.assertEqual(self.VALID_VEHICLE_DATA['price'], vehicle.price)
        self.assertEqual(self.VALID_VEHICLE_DATA['engine'], vehicle.engine)
        self.assertEqual(self.VALID_VEHICLE_DATA['gearbox'], vehicle.gearbox)
        self.assertEqual(self.VALID_VEHICLE_DATA['manufacture_date'], vehicle.manufacture_date)
        self.assertEqual(self.VALID_VEHICLE_DATA['euro_standard'], vehicle.euro_standard)
        self.assertEqual(self.VALID_VEHICLE_DATA['power'], vehicle.power)
        self.assertEqual(self.VALID_VEHICLE_DATA['type'], vehicle.type)
        self.assertEqual(self.VALID_VEHICLE_DATA['mileage'], vehicle.mileage)
        self.assertEqual(self.VALID_VEHICLE_DATA['color'], vehicle.color)
        self.assertEqual(self.VALID_VEHICLE_DATA['condition'], vehicle.condition)
        self.assertEqual(self.VALID_VEHICLE_DATA['location'], vehicle.location)
        self.assertEqual(self.VALID_VEHICLE_DATA['make'], vehicle.make)
        self.assertEqual(self.VALID_VEHICLE_DATA['model'], vehicle.model)

        # Test Fail

    def test_create_vehicle__when_all_is_valid__expect_to_redirect_to_index(self):
        user, profile = self.__create_valid_profile_and_user()
        make, model = self.__create_make_and_model()
        Vehicle.objects.create(**self.VALID_VEHICLE_DATA, make=make, model=model, user=user, )

        response = self.client.post(
            reverse('create vehicle'),
            data=self.VALID_VEHICLE_DATA,
        )

        vehicle = Vehicle.objects.first()

        expected_url = reverse('index')
        self.assertRedirects(response, expected_url)
        self.assertEqual(302, response.status_code)
