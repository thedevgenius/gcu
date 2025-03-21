import json
from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from core.utils import get_hashid
from academics.models import AcademicYear
from .forms import *
from .models import *

hashids = get_hashid(saltname='user_id')
student_hash = get_hashid(saltname='student_id')
# Create your views here.

class SignInView(LoginView):
    template_name = 'accounts/sign_in.html'
    redirect_authenticated_user = True
    form_class = SignInForm

@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = 'accounts/dashboard.html'


class TeacherAddView(TemplateView):
    template_name = 'accounts/teacher_add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TeaheerAddForm()
        return context
    
    def post(self, request):
        form = TeaheerAddForm(request.POST)
        if form.is_valid():
            now = datetime.now()
            data = form.cleaned_data
            dept = data['department']
            last_student = Teacher.objects.filter(department=dept).select_related('user').order_by('-id').first()
            last_student_id = int(last_student.user.username.split('/')[-1]) if last_student else 0
            username = f'GCU/{dept.code}/{now:%y}/{(last_student_id + 1):03d}'
            user = User.objects.create_user(
                username=username,
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                phone=data['phone'],
                date_of_birth=data['date_of_birth'],
                blood_group=data['blood_group'],
            )
            Teacher.objects.create(
                user=user,
                department=dept,
                designation=data['designation']
            )
            Employee.objects.create(
                user=user,
                department='TEA',
                designation=data['designation']
            )
        else:
            print('error')
            return render(request, self.template_name, {'form':form})
        return render(request, self.template_name, self.get_context_data())


@method_decorator(login_required, name='dispatch')
class StudentAddView(TemplateView):
    template_name = 'accounts/student_add.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StudentAddForm
        context['acayear'] = AcademicYear.objects.filter(admission_status=True).first()
        return context
    
    def post(self, request):
        form = StudentAddForm(request.POST)
        if form.is_valid():
            now = datetime.now()
            data = form.cleaned_data
            course = data['course']
            last_student = Student.objects.filter(course=course).select_related('user').order_by('-id').first()
            last_student_id = int(last_student.user.username.split('/')[-1]) if last_student else 0
            username = f'GCU/{course.code}/{now:%y}/{(last_student_id + 1):03d}'
            user = User.objects.create_user(
                username=username,
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                phone=data['phone'],
                date_of_birth=data['date_of_birth'],
                blood_group=data['blood_group'],
            )
            student = Student.objects.create(
                user=user,
                course=course,
                academic_year=self.get_context_data()['acayear'],
                class_roll=last_student_id+1,
                admission_date=now,
                step=2
            )
            return redirect('admission', student.get_hash_id())
        else:
            print(form.errors)

        return render(request, self.template_name, self.get_context_data())


class AdmissionView(FormView):
    template_name = 'accounts/admission.html'
    form_class = AcademicForm  # Default form (not mandatory since we're handling multiple forms)

    def get_student(self, hash_id):
        try:
            student_id = student_hash.decode(hash_id)[0]
            return get_object_or_404(Student, id=student_id)
        except (IndexError, Student.DoesNotExist):
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hash_id = self.kwargs.get('hash_id')
        student = self.get_student(hash_id)
        context['student'] = student
        return context

    def get(self, request, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request):
        context = self.get_context_data()
        student = context['student']
        
        return render(request, self.template_name, context)
    
    
# class AdmissionListView(TemplateView):
#     template_name = 'accounts/admission_list.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['students'] = Student.objects.all().select_related('user')
#         return context
    

