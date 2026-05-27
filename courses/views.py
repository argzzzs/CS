from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Course
from .forms import CourseForm


def course_list(request):
    query = request.GET.get('q', '')
    courses = Course.objects.all()
    if query:
        courses = courses.filter(Q(name__icontains=query) | Q(code__icontains=query))
    return render(request, 'courses/list.html', {'courses': courses, 'query': query})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    enrollments = course.enrollment_set.select_related('student').all()
    return render(request, 'courses/detail.html', {'course': course, 'enrollments': enrollments})


def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course added successfully.')
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'courses/form.html', {'form': form, 'title': 'Add Course'})


def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course updated successfully.')
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/form.html', {'form': form, 'title': 'Edit Course', 'object': course})


def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course deleted.')
        return redirect('course_list')
    return render(request, 'courses/confirm_delete.html', {'object': course, 'type': 'Course'})
