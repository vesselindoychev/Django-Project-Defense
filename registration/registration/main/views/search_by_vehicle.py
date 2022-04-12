from django.core.paginator import Paginator
from django.shortcuts import render

from registration.main.filters import VehicleFilter
from registration.main.models import CarModel, Vehicle


def load_car_models(request):
    make_id = request.GET.get('make')
    car_models = CarModel.objects.filter(make_id=make_id).order_by('name')
    context = {
        'car_models': car_models,
    }
    return render(request, 'main/car_models_dropdown_list.html', context)


# def search_vehicles_form(request):
#     # return render(request, 'main/search-vehicles.html')
#     if request.method == 'POST':
#         # try () instead [] if doesn't work
#         searched = request.POST.get('searched')
#         vehicles = PublishedAdvert.objects.filter(advert__car__make__contains=searched)
#         # my_filter = OrderFilter()
#
#         context = {
#             'searched': searched,
#             'vehicles': vehicles,
#             # 'my_filter': my_filter,
#
#         }
#         return render(request, 'main/search-vehicles.html', context)
#
#     else:
#         context = {}
#         return render(request, 'main/search-vehicles.html', context)
#

def search_by_vehicle_props(request):
    filtered_vehicles = VehicleFilter(
        request.GET,
        queryset=Vehicle.objects.all()
    )

    context = {
        'filtered_vehicles': filtered_vehicles,
    }

    return render(request, 'main/search-form.html', context)


def search_vehicles(request):
    filtered_vehicles = VehicleFilter(
        request.GET,
        queryset=Vehicle.objects.all()
    )

    paginated_filtered_vehicles = Paginator(filtered_vehicles.qs, 4)
    page_number = request.GET.get('page')
    vehicle_page_obj = paginated_filtered_vehicles.get_page(page_number)

    context = {
        'filtered_vehicles': filtered_vehicles,
        'vehicle_page_obj': vehicle_page_obj,
    }

    return render(request, 'main/search-vehicles.html', context)
