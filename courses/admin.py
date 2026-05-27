from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'units', 'instructor', 'date_added']
    search_fields = ['code', 'name', 'instructor']
