from django.views import generic as views

from registration.main.models import PublishedAdvert


class HomeTemplateView(views.TemplateView):
    template_name = 'index.html'


class ShowDashboardListView(views.ListView):
    model = PublishedAdvert
    template_name = 'main/dashboard.html'
    paginate_by = 4


class AboutPageTemplateView(views.TemplateView):
    template_name = 'main/about-us-page.html'
