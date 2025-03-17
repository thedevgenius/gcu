from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import SignInView, DashboardView, StudentAddView, AdmissionView, TeacherAddView


urlpatterns = [
    path('', SignInView.as_view(), name='sign_in'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('student/add/', StudentAddView.as_view(), name='student_add'),
    path('student/<str:hash_id>/', AdmissionView.as_view(), name='admission'),
    # path('admission/list/', AdmissionListView.as_view(), name='admission_list'),
    path('teacher/add/', TeacherAddView.as_view(), name='teacher_add'),
]

