from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from registration.common.validators import validate_car_model, validate_only_letters

UserModel = get_user_model()


class Make(models.Model):
    MAKE_NAME_MAX_LENGTH = 30
    MAKE_NAME_MIN_LENGTH = 2

    name = models.CharField(
        max_length=MAKE_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(MAKE_NAME_MIN_LENGTH),
        ),
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    MODEL_NAME_MAX_LENGTH = 30
    MODEL_NAME_MIN_LENGTH = 3

    make = models.ForeignKey(
        Make,
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        max_length=MODEL_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(MODEL_NAME_MIN_LENGTH),
        ),
    )

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    MIN_PRICE = 0
    LOCATION_MAX_LENGTH = 20
    LOCATION_MIN_LENGTH = 5
    MILEAGE_MIN_VALUE = 0
    COLOR_MAX_LENGTH = 20
    ADDITIONAL_INFO_MAX_LENGTH = 50
    ADDITIONAL_INFO_MIN_LENGTH = 5

    DIESEL = 'Diesel'
    GASOLINE = 'Gasoline'
    ELECTRIC = 'Electric'
    GAS = 'Gas'

    ENGINE = (
        DIESEL,
        GASOLINE,
        ELECTRIC,
        GAS,
    )

    EURO1 = 'Euro 1'
    EURO2 = 'Euro 2'
    EURO3 = 'Euro 3'
    EURO4 = 'Euro 4'
    EURO5 = 'Euro 5'
    EURO6 = 'Euro 6'

    EUROSTANDARDS = (
        EURO1,
        EURO2,
        EURO3,
        EURO4,
        EURO5,
        EURO6,
    )

    MANUAL_TRANSMISSION = 'Manual Transmission'
    AUTOMATIC_TRANSMISSION = 'Automatic Transmission'

    TRANSMISSIONS = (
        MANUAL_TRANSMISSION,
        AUTOMATIC_TRANSMISSION,
    )

    SEDAN = 'Sedan'
    COUPE = 'Coupe'
    STATION_WAGON = 'Station Wagon'
    HATCHBACK = 'Hatchback'
    SUV = 'SUV'
    MINIVAN = 'Minivan'
    PICKUP_TRUCK = 'Pickup Truck'
    VAN = 'Van'
    CONVERTIBLE = 'Convertible'

    TYPES = (
        SEDAN,
        COUPE,
        STATION_WAGON,
        HATCHBACK,
        SUV,
        MINIVAN,
        PICKUP_TRUCK,
        VAN,
        CONVERTIBLE,
    )

    # BLACK = 'Black'
    # BLUE = 'Blue'
    # SILVER = 'Silver'
    # BROWN = 'Brown'
    # RED = 'Red'
    # ORANGE = 'Orange'
    # ORANGE_RED = 'Orange red'
    # YELLOW = 'Yellow'
    # PINK = 'Pink'
    # GREEN = 'Green'
    #
    # COLORS = (
    #
    # )

    PLOVDIV = 'Plovdiv'
    SOFIA = 'Sofia'
    BURGAS = 'Burgas'
    VELIKO_TURNOVO = 'Veliko Turnovo'
    VARNA = 'Varna'
    PAZARDZHIK = 'Pazardzhik'
    YAMBOL = 'Yambol'
    BLAGOEVGRAD = 'Blagoevgrad'
    PERNIK = 'Pernik'
    STARA_ZAGORA = 'Stara Zagora'
    KARLOVO = 'Karlovo'
    HASKOVO = 'Haskovo'
    SLIVEN = 'Sliven'
    RUSE = 'Ruse'

    CITIES = (
        PLOVDIV,
        SOFIA,
        BURGAS,
        VARNA,
        VELIKO_TURNOVO,
        PAZARDZHIK,
        YAMBOL,
        BLAGOEVGRAD,
        PERNIK,
        STARA_ZAGORA,
        KARLOVO,
        HASKOVO,
        SLIVEN,
        RUSE,
    )

    NEW = 'New'
    USED = 'Used'

    CONDITION = (
        NEW,
        USED,
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(MIN_PRICE),
        ),
    )

    engine = models.CharField(
        max_length=max(len(e) for e in ENGINE),
        choices=((e, e) for e in ENGINE),
    )

    gearbox = models.CharField(
        max_length=max(len(t) for t in TRANSMISSIONS),
        choices=((t, t) for t in TRANSMISSIONS),
    )
    YEARS = [i for i in range(2000, 2023)]
    manufacture_date = models.IntegerField(
        choices=((i, i) for i in YEARS),
    )

    euro_standard = models.CharField(
        max_length=max(len(e) for e in EUROSTANDARDS),
        choices=((s, s) for s in EUROSTANDARDS),
    )

    power = models.IntegerField()

    type = models.CharField(
        max_length=max(len(t) for t in TYPES),
        choices=((t, t) for t in TYPES),
    )

    mileage = models.IntegerField(
        validators=(
            MinValueValidator(MILEAGE_MIN_VALUE),
        ),
    )

    color = models.CharField(
        max_length=COLOR_MAX_LENGTH,
        validators=(validate_only_letters,),
    )

    technical_characteristic = models.URLField(
        null=True,
        blank=True,
    )

    condition = models.CharField(
        max_length=max(len(c) for c in CONDITION),
        choices=((c, c) for c in CONDITION),
    )

    location = models.CharField(
        max_length=max(len(c) for c in CITIES),
        choices=((c, c) for c in CITIES),
    )

    additional_info = models.CharField(
        max_length=ADDITIONAL_INFO_MAX_LENGTH,
        validators=(
            MinLengthValidator(ADDITIONAL_INFO_MIN_LENGTH),
        ),
        null=True,
        blank=True,
    )

    # Added additional info
    # Vehicle model done
    # create_vehicle form and view and template done
    # Search form is not done
    # Need to add some additional fixes into templates

    make = models.ForeignKey(
        Make,
        on_delete=models.SET_NULL,
        null=True,
    )

    model = models.ForeignKey(
        CarModel,
        on_delete=models.SET_NULL,
        null=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.make} {self.model}'


class Advert(models.Model):
    image = models.ImageField()
    date_of_publication = models.DateTimeField(
        auto_now_add=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )

    car = models.OneToOneField(
        Vehicle,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.car.make} {self.car.model}'


class PublishedAdvert(models.Model):
    likes = models.IntegerField(
        default=0,
        null=True,
        blank=True,
    )

    advert = models.OneToOneField(
        Advert,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.advert.car.make} {self.advert.car.model}'

    class Meta:
        ordering = ('-id',)


class Contact(models.Model):
    SUBJECT_MAX_LENGTH = 50
    SUBJECT_MIN_LENGTH = 5
    email = models.EmailField()
    subject = models.CharField(
        max_length=SUBJECT_MAX_LENGTH,
        validators=(
            MinLengthValidator(SUBJECT_MIN_LENGTH),
        ),
    )
    message = models.TextField()

    # user = models.ForeignKey(
    #     UserModel,
    #     on_delete=models.CASCADE,
    # )

    def __str__(self):
        return self.email


class FeedBack(models.Model):
    TOPIC_MAX_LENGTH = 30
    TOPIC_MIN_LENGTH = 5
    VERY_SATISFIED = 'Very satisfied'
    SATISFIED = 'Satisfied'
    NEITHER_AGREE_NOR_DISAGREE = 'Neither agree nor disagree'
    DISSATISFIED = 'Dissatisfied'
    VERY_DISSATISFIED = 'Very dissatisfied'

    STATUS = (
        VERY_SATISFIED,
        SATISFIED,
        NEITHER_AGREE_NOR_DISAGREE,
        DISSATISFIED,
        VERY_DISSATISFIED,
    )

    status = models.CharField(
        max_length=max(len(s) for s in STATUS),
        choices=((s, s) for s in STATUS),
    )

    email = models.EmailField()
    topic = models.CharField(
        max_length=TOPIC_MAX_LENGTH,
        validators=(
            MinLengthValidator(TOPIC_MIN_LENGTH),
        ),
    )
    message = models.TextField()

    # user = models.ForeignKey(
    #     UserModel,
    #     on_delete=models.CASCADE,
    # )
