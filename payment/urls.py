
from django.urls import path

from .views import FeeAddView, FeeListView

urlpatterns = [
    path('<str:course_code>/fee/add/', FeeAddView.as_view(), name='course_fee_add'),
    path('<str:course_code>/fees/', FeeListView.as_view(), name='course_fee_list'),
]

