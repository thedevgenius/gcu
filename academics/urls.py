from django.urls import path

from .views import DepartmentAddView, DepartmentListView, ChangeDepartmentStatus, CourseAddView, CourseListView, CourseEditView, CourseDetailsView, AcademicYearView, SemesterView, GetScheduleFormView
#Create your urls here

urlpatterns = [
    path('department/add/', DepartmentAddView.as_view(), name='department_add'),
    path('department/list/', DepartmentListView.as_view(), name='department_list'),
    path('change-dept-status/', ChangeDepartmentStatus.as_view(), name='change_status'),
    path('course/add/', CourseAddView.as_view(), name='course_add'),
    path('course/list/', CourseListView.as_view(), name='course_list'),
    path('course/edit/<int:pk>/', CourseEditView.as_view(), name='course_edit'),
    path('course/<str:code>/', CourseDetailsView.as_view(), name='course_detail'),
    path('academic-years/', AcademicYearView.as_view(), name='academic_year'),
    path('<str:code>/<int:no>/', SemesterView.as_view(), name='semester'),
    path('open-schedule-form/', GetScheduleFormView.as_view(), name='get_schedule_form'),
]