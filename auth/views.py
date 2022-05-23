from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from auth.forms import RegisterForm


# Create your views here.

class Register(CreateView):
    """
    For registration we use the fields from the registration form
    """
    form_class = RegisterForm
    
    template_name = "register/registration.html"
    success_url = reverse_lazy("home")
