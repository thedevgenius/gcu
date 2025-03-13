from django.shortcuts import render
from django.views.generic import TemplateView

from academics.models import Course
from .models import FeeCategory, Fee
from .forms import FeeAddForm
# Create your views here.
class FeeAddView(TemplateView):
    template_name = 'payment/fee_add.html'

    def get_course(self, **kwargs):
        code=kwargs.get('course_code')
        return Course.objects.filter(code=code).first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['feecats'] = FeeCategory.objects.all()
        context['form'] = FeeAddForm()
        return context
    
    def get(self, request, **kwargs):
        context = self.get_context_data()
        context['course'] = self.get_course(**kwargs)
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        form = FeeAddForm(request.POST)
        context = self.get_context_data()
        context['course'] = self.get_course(**kwargs)
        context['form'] = form
        if form.is_valid():
            fee = Fee.objects.create(
                title=form.cleaned_data['title'],
                course=context['course'],
                due_date=form.cleaned_data['due_date'],
                breakdown=form.cleaned_data['breakdown']
            )
        else:
            print(form.errors)
        
        return render(request, self.template_name, context)