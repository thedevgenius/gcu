from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy

from .models import Department
from .forms import DepartmentAddForm
# Create your views here.

class DepartmentAddView(CreateView):
    template_name = 'academics/department_add.html'
    model = Department
    form_class = DepartmentAddForm
    success_url = '/department/list/'

class DepartmentListView(ListView):
    template_name = 'academics/department_list.html'
    model = Department
    context_object_name = 'departments'

class DepartmentEditView(UpdateView):
    template_name = 'academics/department_edit.html'
    model = Department
    form_class = DepartmentAddForm
    success_url = reverse_lazy('department_list')
    

