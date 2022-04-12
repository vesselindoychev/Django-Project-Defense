from django.urls import reverse_lazy
from django.views import generic as views

from registration.accounts.models import Profile
from registration.main.forms.advert import CreateAdvertForm, EditAdvertForm, DeleteAdvertForm
from registration.main.models import Advert


class ShowAdvertsDetailView(views.DetailView):
    model = Profile
    template_name = 'main/show-adverts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        adverts = list(Advert.objects.filter(user_id=self.object.user_id))
        context['adverts'] = adverts
        return context


class CreateAdvertView(views.CreateView):
    form_class = CreateAdvertForm
    template_name = 'main/advert-create.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditAdvertView(views.UpdateView):
    model = Advert
    form_class = EditAdvertForm
    template_name = 'main/advert-edit.html'

    def get_success_url(self):
        return reverse_lazy('show advert details', kwargs={'pk': self.object.pk})


class DeleteAdvertView(views.DeleteView):
    model = Advert
    form_class = DeleteAdvertForm
    template_name = 'main/advert-delete.html'

    def get_success_url(self):
        return reverse_lazy('show adverts', kwargs={'pk': self.object.user_id})


class ShowDetailsAdvertDetailView(views.DetailView):
    model = Advert
    template_name = 'main/show-advert-details.html'
