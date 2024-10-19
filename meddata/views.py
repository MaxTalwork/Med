from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from meddata.forms import AppointmentForm, DoctorForm, MedServiceForm, ClientAppointmentForm
from meddata.models import Appointment, Doctor, MedService


def home(request):
    return render(request, "meddata/home.html")


def main(request):
    return render(request, "meddata/main.html")


class MedServiceCreateView(CreateView):
    model = MedService
    form_class = MedServiceForm
    success_url = reverse_lazy("meddata:medservice_list")


class MedServiceListView(ListView):
    model = MedService

    def get_queryset(self):
        return MedService.objects.all()

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        list_product = MedService.objects.all()
        context_data["object_list"] = list_product
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
    success_url = reverse_lazy("meddata:medservice_list")


class MedServiceDeleteView(DeleteView):
    model = MedService
    success_url = reverse_lazy("meddata:medservice_list")


class DoctorCreateView(CreateView):
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy("meddata:doctor_list")


class DoctorListView(ListView):
    model = Doctor

    def get_queryset(self):
        return Doctor.objects.all()

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        list_product = Doctor.objects.all()
        context_data["object_list"] = list_product
        return context_data


class DoctorDetailView(DetailView):
    model = Doctor

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.save()
        return self.object


class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy("meddata:doctor_list")


class DoctorDeleteView(DeleteView):
    model = Doctor
    success_url = reverse_lazy("meddata:doctor_list")


class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy("meddata:appointment_list")


class AppointmentListView(ListView):
    model = Appointment

    def get_queryset(self):
        return Appointment.objects.all()

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        list_product = Appointment.objects.all()
        context_data["object_list"] = list_product
        return context_data


class AppointmentDetailView(DetailView):
    model = Appointment

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.save()
        return self.object


class AppointmentUpdateView(UpdateView):
    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy("meddata:appointment_list")


class ClientAppointmentUpdateView(UpdateView):
    model = Appointment
    form_class = ClientAppointmentForm
    success_url = reverse_lazy("meddata:appointment_list")


class AppointmentDeleteView(DeleteView):
    model = Appointment
    success_url = reverse_lazy("meddata:appointment_list")
