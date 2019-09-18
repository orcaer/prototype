from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from braces.views import SelectRelatedMixin
from django.urls import reverse_lazy
from . import forms
from . import filters
from trips.models import Trip


from . import forms
from . import models

# Create your views here.
class CreateRequest(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    # fields = ('destination', 'address', 'date')
    form_class = forms.RequestsForm
    model = models.Requests

    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class ListRequests(generic.ListView):
    model = Trip
    template_name = 'requests/select_request.html'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = filters.TripFilter(self.request.GET, queryset = self.get_queryset())
        return context
