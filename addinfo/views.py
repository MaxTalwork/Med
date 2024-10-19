from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from addinfo.forms import ComTextForm, FeedbackForm
from addinfo.models import ComText, Feedback


class ComTextCreateView(CreateView):
    model = ComText
    form_class = ComTextForm
    success_url = reverse_lazy("addinfo:comtext_list")


class ComTextListView(ListView):
    model = ComText

    def get_queryset(self):
        return ComText.objects.all()

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        list_product = ComText.objects.all()
        context_data["object_list"] = list_product
        return context_data


class ComTextDetailView(DetailView):
    model = ComText

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.save()
        return self.object


class ComTextUpdateView(UpdateView):
    model = ComText
    form_class = ComTextForm
    success_url = reverse_lazy("addinfo:comtext_list")


class ComTextDeleteView(DeleteView):
    model = ComText
    success_url = reverse_lazy("addinfo:comtext_list")


class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    success_url = reverse_lazy("addinfo:feedback_list")


class FeedbackListView(ListView):
    model = Feedback

    def get_queryset(self):
        return Feedback.objects.all()

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        list_product = Feedback.objects.all()
        context_data["object_list"] = list_product
        return context_data


class FeedbackDetailView(DetailView):
    model = Feedback

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.save()
        return self.object


class FeedbackUpdateView(UpdateView):
    model = Feedback
    form_class = FeedbackForm
    success_url = reverse_lazy("addinfo:feedback_list")


class FeedbackDeleteView(DeleteView):
    model = Feedback
    success_url = reverse_lazy("addinfo:feedback_list")
