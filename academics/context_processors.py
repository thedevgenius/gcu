from .models import Department

def academics_data(request):
    total_department = Department.objects.filter(status=True).count()
    context = {
        'total_department' : total_department
    }
    return context