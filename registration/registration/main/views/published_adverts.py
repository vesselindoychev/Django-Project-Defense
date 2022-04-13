from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from registration.main.models import PublishedAdvert


class PublishAdvertCreateView(views.CreateView):
    model = PublishedAdvert
    template_name = 'main/published-advert-create.html'
    success_url = reverse_lazy('show dashboard')
    fields = ('advert',)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PublishedAdvertDetailsView(views.DetailView):
    model = PublishedAdvert
    template_name = 'main/published-advert-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.object.user == self.request.user
        return context

def like_advert(request, pk):
    advert = PublishedAdvert.objects.get(pk=pk)
    advert.likes += 1
    advert.save()
    return redirect('published advert details', pk)