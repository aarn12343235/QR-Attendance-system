from django.urls import path
from attendance_app import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # API Paths
    path('api/login/student/', views.student_login_api, name='api_student_login'),
    path('api/login/teacher/', views.teacher_login_api, name='api_teacher_login'),
    path('api/attendance/mark/', views.mark_attendance_api, name='api_mark_attendance'),
]