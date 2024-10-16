from django.contrib import admin

from meddata.models import Appointment, Doctor, MedBranch, MedService


@admin.register(MedService)
class MedServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "med_branch")
    list_filter = ("med_branch",)
    search_fields = ("name", "description")


@admin.register(MedBranch)
class MedBranchAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ("surname", "name", "patronymic", "med_branch")


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "med_service", "doctor", "med_branch", "end_date", "client")
    list_filter = ("id", "med_service", "doctor", "med_branch", "end_date", "client")
    search_fields = ("name", "description")
