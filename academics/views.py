from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import CreateView, ListView, UpdateView, TemplateView
from django.views import View
from django.urls import reverse_lazy
from django.template.loader import render_to_string

from .models import Department, Course, AcademicYear
from .forms import DepartmentAddForm, CourseAddForm
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_depertment'] = Department.objects.all().count()
        return context


class DepartmentEditView(UpdateView):
    template_name = 'academics/department_edit.html'
    model = Department
    form_class = DepartmentAddForm
    success_url = reverse_lazy('department_list')


class CourseAddView(CreateView):
    template_name = 'academics/course_add.html'
    model = Course
    form_class = CourseAddForm
    success_url = reverse_lazy('course_list')


class CourseListView(ListView):
    template_name = 'academics/course_list.html'
    model = Course
    context_object_name = 'courses'

    def get_queryset(self):
        return super().get_queryset().select_related('department').order_by('department__name', 'name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_course'] = Course.objects.all().count()
        return context
            

class CourseEditView(UpdateView):
    template_name = 'academics/course_edit.html'
    model = Course
    form_class = CourseAddForm
    success_url = reverse_lazy('course_list')


class AcademicYearView(TemplateView):
    template_name = 'academics/academic_year.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['acys'] = AcademicYear.objects.all()
        return context
    