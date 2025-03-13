
from django.urls import path

from .views import FeeAddView

urlpatterns = [
    path('<str:course_code>/fee/add/', FeeAddView.as_view(), name='course_fee_add'),
    
]

