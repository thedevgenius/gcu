from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, TemplateView
from django.views import View
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.db import IntegrityError

# from payment.models import Fee
from accounts.models import Teacher
from .models import Department, Course, AcademicYear, Subject, Schedule
from .forms import DepartmentAddForm, CourseAddForm
# Create your views here.

class DepartmentAddView(View):
    def get(self, request):
        id = request.GET.get('id')
        department = Department.objects.get(id=id)
        form = DepartmentAddForm(instance=department)  # Adjust fields as necessary
        from django.template.context_processors import csrf
        context = {'form': form}
        context.update(csrf(request))
        html = render_to_string('academics/department_form.html', context)
        return JsonResponse({'status': True, 'html':html})
    
    def post(self, request, **kwargs):
        id = request.POST.get('id')
        if id:
            department = get_object_or_404(Department, id=id)
            form = DepartmentAddForm(request.POST, instance=department)
        else:
            form = DepartmentAddForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return JsonResponse({'status': False, 'errors': form.errors})

        return JsonResponse({'status': True})


class DepartmentListView(ListView):
    template_name = 'academics/department_list.html'
    model = Department
    context_object_name = 'departments'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_depertment'] = Department.objects.all().count()
        context['form'] = DepartmentAddForm()
        return context


class ChangeDepartmentStatus(View):
    def post(self, request):
        id = request.POST.get('id')
        department = get_object_or_404(Department, id=id)
        if department:
            department.status = not department.status
            department.save()
            return JsonResponse({'success':True})
        else:
            return JsonResponse({'success':False})

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


class CourseDetailsView(TemplateView):
    template_name = 'academics/course_detail.html'
    
    def get_course(self, code):
        try:
            return get_object_or_404(Course, code=code)
        except (IndexError, Course.DoesNotExist):
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        code = self.kwargs.get('code')
        course = self.get_course(code)
        context['course'] = course
        # context['fees'] = Fee.objects.filter(course=course, academic_year__is_open=True)
        return context

    def get(self, request, **kwargs):
        return render(request, self.template_name, self.get_context_data())


class AcademicYearView(TemplateView):
    template_name = 'academics/academic_year.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['acys'] = AcademicYear.objects.all()
        return context
    
class SemesterView(TemplateView):
    template_name = 'academics/semester.html'

    def get_course(self, **kwargs):
        code = kwargs.get('code')
        course = Course.objects.get(code=code)
        return course

    def get(self, request, **kwargs):
        context = {}
        semester = kwargs.get('no')
        context['semester'] = semester
        context['course'] = self.get_course(**kwargs)
        schedules = Schedule.objects.filter(course=context['course'], semester=semester)
        request.session['course_id'] = context['course'].id
        request.session['semester'] = semester
        
        return render(request, self.template_name, context)
    
    
    


class GetScheduleFormView(View):
    def get(self, request):
        from django.template.context_processors import csrf
        code = request.GET.get('code')
        semester = request.GET.get('semester')
        course = Course.objects.get(code=code)
        request.session['day'] = request.GET.get('day')
        request.session['period'] = request.GET.get('period')
        subjects = Subject.objects.filter(course=course, semester=semester)
        teachers = Teacher.objects.all()
        
        context = {'subjects':subjects, 'teachers': teachers}
        context.update(csrf(request))
        
        html = render_to_string('academics/schedule_form.html', context)
        return JsonResponse({'html': html})
    
    def post(self, request):
        data = request.POST
        print(data)
        course = Course.objects.get(id=request.session['course_id'])
        print(course)
        print(request.session['semester'])
        return JsonResponse({'success':True})
    

