from django.contrib import admin
from .models import Student, Enrollment


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_id', 'last_name', 'first_name', 'year_level', 'email', 'date_registered']
    search_fields = ['student_id', 'first_name', 'last_name']
    list_filter = ['year_level']


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'date_enrolled', 'status']
    list_filter = ['status', 'course']
    search_fields = ['student__first_name', 'student__last_name', 'course__code']
