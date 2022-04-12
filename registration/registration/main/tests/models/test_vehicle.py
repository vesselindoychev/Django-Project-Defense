from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from registration.main.models import Vehicle

UserModel = get_user_model()


class VehicleTests(TestCase):
    VALID_VEHICLE_DATA = {
        'price': 3200.0,
        'engine': 'Diesel',
        'gearbox': 'Manual Transmission',
        'manufacture_date': 2004,
        'euro_standard': 'Euro 1',
        'power': 112,
        'type': 'Sedan',
        'mileage': 203123,
        'color': 'Black',
        'condition': 'Used',
        'location': 'Plovdiv',
        'make_id': 1,
        'model_id': 1,
        'user_id': 6,
    }

    def test_vehicle_create__when_color_contains_only_letters__expect_success(self):
        vehicle = Vehicle(
            **self.VALID_VEHICLE_DATA,
        )

        vehicle.save()

    def test_vehicle_create__when_color_contains_a_digit__expect_to_fail(self):
        color = 'Bla ck1'

        vehicle = Vehicle(
            color=color,
            price=self.VALID_VEHICLE_DATA['price'],
            engine=self.VALID_VEHICLE_DATA['engine'],
            gearbox=self.VALID_VEHICLE_DATA['gearbox'],
            manufacture_date=self.VALID_VEHICLE_DATA['manufacture_date'],
            euro_standard=self.VALID_VEHICLE_DATA['euro_standard'],
            power=self.VALID_VEHICLE_DATA['power'],
            type=self.VALID_VEHICLE_DATA['type'],
            mileage=self.VALID_VEHICLE_DATA['mileage'],
            condition=self.VALID_VEHICLE_DATA['condition'],
            location=self.VALID_VEHICLE_DATA['location'],
            make_id=self.VALID_VEHICLE_DATA['make_id'],
            model_id=self.VALID_VEHICLE_DATA['model_id'],
            user_id=self.VALID_VEHICLE_DATA['user_id'],
        )

        with self.assertRaises(ValidationError) as context:
            vehicle.full_clean()
            vehicle.save()

        self.assertIsNotNone(context.exception)

    def test_vehicle_create__when_color_contains_space__expect_to_fail(self):
        color = 'Bl ack'

        vehicle = Vehicle(
            color=color,
            price=self.VALID_VEHICLE_DATA['price'],
            engine=self.VALID_VEHICLE_DATA['engine'],
            gearbox=self.VALID_VEHICLE_DATA['gearbox'],
            manufacture_date=self.VALID_VEHICLE_DATA['manufacture_date'],
            euro_standard=self.VALID_VEHICLE_DATA['euro_standard'],
            power=self.VALID_VEHICLE_DATA['power'],
            type=self.VALID_VEHICLE_DATA['type'],
            mileage=self.VALID_VEHICLE_DATA['mileage'],
            condition=self.VALID_VEHICLE_DATA['condition'],
            location=self.VALID_VEHICLE_DATA['location'],
            make_id=self.VALID_VEHICLE_DATA['make_id'],
            model_id=self.VALID_VEHICLE_DATA['model_id'],
            user_id=self.VALID_VEHICLE_DATA['user_id'],
        )

        with self.assertRaises(ValidationError) as context:
            vehicle.full_clean()
            vehicle.save()

        self.assertIsNotNone(context.exception)

    def test_vehicle_create__when_color_contains_dollar__expect_to_fail(self):
        color = 'Black$'

        vehicle = Vehicle(
            color=color,
        )

        with self.assertRaises(ValidationError) as context:
            vehicle.full_clean()
            vehicle.save()
        self.assertIsNotNone(context.exception)
