from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student, Teacher, Attendance
import json
import datetime

def index(request):
    return render(request, 'attendance_app/index.html')



@csrf_exempt
def student_login_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        # Create or Update the student in the Real DB
        student, created = Student.objects.update_or_create(
            student_id=data['id'],
            defaults={
                'first_name': data['firstname'],
                'last_name': data['lastname'],
                'course': data['course'],
                'level': data['level']
            }
        )
        return JsonResponse({'status': 'success', 'message': 'Student Profile Loaded'})
    return JsonResponse({'status': 'error'}, status=400)

@csrf_exempt
def teacher_login_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        # Create or Update the teacher in the Real DB
        teacher, created = Teacher.objects.update_or_create(
            teacher_id=data['id'],
            defaults={
                'first_name': data['firstname'],
                'last_name': data['lastname'],
                'subject': data['subject']
            }
        )
        return JsonResponse({'status': 'success', 'message': 'Teacher Dashboard Loaded'})
    return JsonResponse({'status': 'error'}, status=400)

@csrf_exempt
def mark_attendance_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        scanned_id = data.get('student_id')
        
        try:
            student = Student.objects.get(student_id=scanned_id)
            
            # Check if already marked today
            today = datetime.date.today()
            if Attendance.objects.filter(student=student, date_marked=today).exists():
                return JsonResponse({'status': 'error', 'message': 'Already marked present today!'})
            
            # Save to DB
            Attendance.objects.create(student=student)
            
            return JsonResponse({
                'status': 'success',
                'student': {
                    'name': f"{student.first_name} {student.last_name}",
                    'id': student.student_id,
                    'course_level': f"{student.course} - {student.level}"
                }
            })
            
        except Student.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Student ID not found in database.'})
            
    return JsonResponse({'status': 'error'}, status=400)