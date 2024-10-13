from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from meddata.forms import MedServiceForm
from meddata.models import MedService


def home(request):
    return render(request, "meddata/home.html")

def main(request):
    return render(request, 'meddata/main.html')


class MedServiceCreateView(CreateView):
    model = MedService
    form_class = MedServiceForm
    success_url = reverse_lazy('meddata:medservice_list')


class MedServiceListView(ListView):
    model = MedService

    def get_queryset(self):
        return MedService.objects.all()

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        list_product = MedService.objects.all()
        context_data['object_list'] = list_product
        return context_data


class MedServiceDetailView(DetailView):
    model = MedService

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.save()
        return self.object


class MedServiceUpdateView(UpdateView):
    model = MedService
    form_class = MedServiceForm
    success_url = reverse_lazy('meddata:medservice_list')


class MedServiceDeleteView(DeleteView):
    model = MedService
    success_url = reverse_lazy('meddata:medservice_list')
