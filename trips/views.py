from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from braces.views import SelectRelatedMixin
from django.urls import reverse_lazy
from . import forms


from . import forms
from . import models

# Create your views here.
class CreateTrip(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    # fields = ('destination', 'address', 'date')
    form_class = forms.TripForm
    model = models.Trip

    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class TripConfirm(LoginRequiredMixin, SelectRelatedMixin, generic.DetailView):
    model = models.Trip
    select_related = ('user',)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )
