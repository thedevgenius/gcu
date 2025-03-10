from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView

from .forms import SignInForm
# Create your views here.

class SignInView(LoginView):
    template_name = 'accounts/sign_in.html'
    redirect_authenticated_user = True
    form_class = SignInForm

class DashboardView(TemplateView):
    template_name = 'accounts/dashboard.html'