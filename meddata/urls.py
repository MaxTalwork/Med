from django.urls import path
from django.views.decorators.cache import cache_page

from meddata.apps import MeddataConfig
from meddata.models import MedService
from meddata.views import (AppointmentCreateView, AppointmentDeleteView,
                           AppointmentDetailView, AppointmentListView,
                           AppointmentUpdateView, ClientAppointmentUpdateView,
                           DoctorCreateView, DoctorDeleteView,
                           DoctorDetailView, DoctorListView, DoctorUpdateView,
                           MedServiceCreateView, MedServiceDeleteView,
                           MedServiceDetailView, MedServiceListView,
                           MedServiceUpdateView, home)

app_name = MeddataConfig.name
urlpatterns = [
    path("", home, name="home"),
    path("main/", MedService, name="main"),
    path("medservice_list/", MedServiceListView.as_view(), name="medservice_list"),
    path(
        "medservice/<int:pk>/",
        cache_page(60)(MedServiceDetailView.as_view()),
        name="medservice",
    ),
    path(
        "medservice/create/", MedServiceCreateView.as_view(), name="medservice_create"
    ),
    path(
        "medservice/<int:pk>/update/",
        MedServiceUpdateView.as_view(),
        name="medservice_update",
    ),
    path(
        "medservice/<int:pk>/delete/",
        MedServiceDeleteView.as_view(),
        name="medservice_delete",
    ),
    path("doctor_list/", DoctorListView.as_view(), name="doctor_list"),
    path("doctor/<int:pk>/", cache_page(60)(DoctorDetailView.as_view()), name="doctor"),
    path("doctor/create/", DoctorCreateView.as_view(), name="doctor_create"),
    path("doctor/<int:pk>/update/", DoctorUpdateView.as_view(), name="doctor_update"),
    path("doctor/<int:pk>/delete/", DoctorDeleteView.as_view(), name="doctor_delete"),
    path("appointment_list/", AppointmentListView.as_view(), name="appointment_list"),
    path(
        "appointment/<int:pk>/",
        cache_page(60)(AppointmentDetailView.as_view()),
        name="appointment",
    ),
    path(
        "appointment/create/",
        AppointmentCreateView.as_view(),
        name="appointment_create",
    ),
    path(
        "appointment/<int:pk>/update/",
        AppointmentUpdateView.as_view(),
        name="appointment_update",
    ),
    path(
        "appointment/<int:pk>/update/",
        ClientAppointmentUpdateView.as_view(),
        name="client_appointment_update",
    ),
    path(
        "appointment/<int:pk>/delete/",
        AppointmentDeleteView.as_view(),
        name="appointment_delete",
    ),
]
