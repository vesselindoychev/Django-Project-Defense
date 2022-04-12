from django.urls import reverse, reverse_lazy
from django.views import generic as views

from registration.accounts.models import Profile
from registration.main.forms.vehicle import CreateVehicleForm, EditVehicleForm, DeleteVehicleForm
from registration.main.models import Vehicle


class CreateVehicleView(views.CreateView):
    form_class = CreateVehicleForm
    template_name = 'main/vehicle-create.html'

    # success_url = reverse_lazy('index')

    def get_success_url(self):
        return reverse('index')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditVehicleView(views.UpdateView):
    model = Vehicle
    form_class = EditVehicleForm
    template_name = 'main/vehicle-edit.html'

    def get_success_url(self):
        return reverse_lazy('show adverts', kwargs={'pk': self.object.user_id})


class DeleteVehicleView(views.DeleteView):
    model = Vehicle
    form_class = DeleteVehicleForm
    template_name = 'main/vehicle-delete.html'

    def get_success_url(self):
        return reverse_lazy('show vehicles', kwargs={'pk': self.object.user_id})


class ShowVehicleDetailView(views.DetailView):
    model = Profile
    template_name = 'main/show-vehicles.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vehicles = list(Vehicle.objects.filter(user_id=self.object.user_id))
        context['vehicles'] = vehicles
        return context
