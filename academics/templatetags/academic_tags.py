from django import template
from academics.models import Schedule, Course

register = template.Library()

@register.filter
def get_schedule(value, args):
    day, period, semester = args.split(',')
    course = Course.objects.get(id=value)
    schedules = Schedule.objects.filter(course=course, semester=semester)
    return schedules