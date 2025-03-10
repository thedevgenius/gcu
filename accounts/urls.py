from django.urls import path

from .views import SignInView, DashboardView

urlpatterns = [
    path('', SignInView.as_view(), name='sign_in'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]