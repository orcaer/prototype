from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from . import forms

# Create your views here.

class SignUp(CreateView):
    form_class = forms.SignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy("login")

class LogoutPage(TemplateView):
    template_name = 'logout.html'
    success_url = reverse_lazy("logout")
