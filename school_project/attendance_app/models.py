from django.db import models

class Student(models.Model):
    # Matches your frontend requirements
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    level = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Teacher(models.Model):
    teacher_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_marked = models.DateField(auto_now_add=True)
    time_marked = models.TimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.student_id} - {self.time_marked}"