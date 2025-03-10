from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import SignInView, DashboardView

urlpatterns = [
    path('', SignInView.as_view(), name='sign_in'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
]