from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.views import *
from django.shortcuts import redirect
from django.contrib.auth import logout as auth_logout


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url= reverse_lazy('login')
    template_name= 'registration/signup.html'


class CustomLogoutView(View):
    def post(self, request, *args, **kwargs):
        auth_logout(request) 
        return redirect('/')

    def get(self, request, *args, **kwargs):
        return redirect('/')
    