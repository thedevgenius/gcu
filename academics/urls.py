from django.urls import path

from .views import DepartmentAddView, DepartmentListView, DepartmentEditView, CourseAddView, CourseListView, CourseEditView, AcademicYearView, SettingsView, GradeDetailsView, SubjectAddView
#Create your urls here

urlpatterns = [
    path('department/add/', DepartmentAddView.as_view(), name='department_add'),
    path('department/list/', DepartmentListView.as_view(), name='department_list'),
    path('department/edit/<int:pk>/', DepartmentEditView.as_view(), name='department_edit'),
    path('course/add/', CourseAddView.as_view(), name='course_add'),
    path('course/list/', CourseListView.as_view(), name='course_list'),
    path('course/edit/<int:pk>/', CourseEditView.as_view(), name='course_edit'),
    path('academic-years/', AcademicYearView.as_view(), name='academic_year'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('<str:course_code>/<int:grade_num>/', GradeDetailsView.as_view(), name='grade_details'),
    path('subject-add/', SubjectAddView.as_view(), name='subject_add'),
]