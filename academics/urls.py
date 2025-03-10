from django.urls import path

from .views import DepartmentAddView, DepartmentListView, DepartmentEditView

urlpatterns = [
    path('department/add/', DepartmentAddView.as_view(), name='department_add'),
    path('department/list/', DepartmentListView.as_view(), name='department_list'),
    path('department/edit/<int:pk>/', DepartmentEditView.as_view(), name='department_edit'),
]