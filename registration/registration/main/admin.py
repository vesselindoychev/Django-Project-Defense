from django.contrib import admin

from registration.main.models import Vehicle, Contact, Advert, PublishedAdvert, FeedBack, Make, CarModel


@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    pass


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('make', 'name', )
    ordering = ('make', )


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    pass


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    pass


@admin.register(PublishedAdvert)
class PublishedAdvertAdmin(admin.ModelAdmin):
    pass


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('status', 'email',)


admin.site.register(Contact)
