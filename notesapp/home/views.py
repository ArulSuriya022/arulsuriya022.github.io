from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

# Create your views here.

class SignupView(CreateView):
    form_class = UserCreationForm
    print(form_class,'hgfjysfdj')
    template_name = 'home/register.html'
    success_url = 'smart/notes'
    print(success_url)

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)

class SignupInterfaceView(TemplateView):
    template_name = 'home/register.html'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class HomeView(TemplateView):
    template_name = 'home/welcome.html'

