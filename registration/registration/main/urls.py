from django.urls import path

from registration.main.views.adverts import CreateAdvertView, EditAdvertView, DeleteAdvertView, ShowAdvertsDetailView, \
    ShowDetailsAdvertDetailView
from registration.main.views.contact_and_feedbacks import contact_view, leave_feedback
from registration.main.views.generic import HomeTemplateView, ShowDashboardListView, AboutPageTemplateView
from registration.main.views.published_adverts import PublishAdvertCreateView, PublishedAdvertDetailsView
from registration.main.views.search_by_vehicle import load_car_models, search_vehicles, search_by_vehicle_props
from registration.main.views.vehicles import CreateVehicleView, ShowVehicleDetailView, EditVehicleView, \
    DeleteVehicleView

urlpatterns = (

    # Home
    path('', HomeTemplateView.as_view(), name='index'),

    # Vehicle
    path('vehicle/create/', CreateVehicleView.as_view(), name='create vehicle'),
    path('show-vehicles/<int:pk>/', ShowVehicleDetailView.as_view(), name='show vehicles'),
    path('vehicle/edit/<int:pk>/', EditVehicleView.as_view(), name='edit vehicle'),
    path('vehicle/delete/<int:pk>/', DeleteVehicleView.as_view(), name='delete vehicle'),
    path('ajax/load-car-models/', load_car_models, name='ajax load car models'),

    # Advert
    path('advert/create/', CreateAdvertView.as_view(), name='create advert'),
    path('advert/edit/<int:pk>/', EditAdvertView.as_view(), name='edit advert'),
    path('advert/delete/<int:pk>/', DeleteAdvertView.as_view(), name='delete advert'),
    path('show-adverts/<int:pk>/', ShowAdvertsDetailView.as_view(), name='show adverts'),
    path('show-adverts-details/<int:pk>/', ShowDetailsAdvertDetailView.as_view(), name='show advert details'),

    # Publish Advert
    path('publish-advert/create/', PublishAdvertCreateView.as_view(), name='publish advert create'),
    path('published-advert/details/<int:pk>/', PublishedAdvertDetailsView.as_view(), name='published advert details'),

    # Dashboard
    path('show-dashboard/', ShowDashboardListView.as_view(), name='show dashboard'),

    # Contact
    path('contact/', contact_view, name='contact'),
    path('leave-feedback/', leave_feedback, name='leave feedback'),

    # Search
    path('search-vehicle/', search_vehicles, name='search vehicle'),
    path('show-search-form/', search_by_vehicle_props, name='show search form'),

    # About Us Page
    path('about-us/', AboutPageTemplateView.as_view(), name='about us page')

)
