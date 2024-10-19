from django.core.exceptions import ValidationError
from django.forms import BooleanField, ModelForm

from meddata.models import Appointment, Doctor, MedService


class StyleFormMixin(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


class MedServiceForm(StyleFormMixin, ModelForm):
    class Meta:
        model = MedService
        fields = "__all__"


class DoctorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"


class AppointmentForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"


class ClientAppointmentForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Appointment
        fields = ("client",)
