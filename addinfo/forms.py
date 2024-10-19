from django.core.exceptions import ValidationError
from django.forms import BooleanField, ModelForm

from addinfo.models import ComText, Feedback


class StyleFormMixin(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


class ComTextForm(StyleFormMixin, ModelForm):
    class Meta:
        model = ComText
        fields = "__all__"


class FeedbackForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Feedback
        fields = "__all__"
