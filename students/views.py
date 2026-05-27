from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Student, Enrollment
from .forms import StudentForm, EnrollmentForm
from courses.models import Course


def dashboard(request):
    context = {
        'total_courses': Course.objects.count(),
        'total_students': Student.objects.count(),
        'total_enrollments': Enrollment.objects.count(),
        'recent_enrollments': Enrollment.objects.select_related('student', 'course').all()[:10],
    }
    return render(request, 'home.html', context)


# --- Student CRUD ---

def student_list(request):
    query = request.GET.get('q', '')
    year = request.GET.get('year', '')
    students = Student.objects.all()
    if query:
        students = students.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(student_id__icontains=query)
        )
    if year:
        students = students.filter(year_level=year)
    return render(request, 'students/list.html', {'students': students, 'query': query, 'year': year})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    enrollments = student.enrollment_set.select_related('course').all()
    return render(request, 'students/detail.html', {'student': student, 'enrollments': enrollments})


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully.')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/form.html', {'form': form, 'title': 'Add Student'})


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully.')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/form.html', {'form': form, 'title': 'Edit Student', 'object': student})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted.')
        return redirect('student_list')
    return render(request, 'students/confirm_delete.html', {'object': student, 'type': 'Student'})


# --- Enrollment CRUD ---

def enrollment_list(request):
    course_filter = request.GET.get('course', '')
    status_filter = request.GET.get('status', '')
    enrollments = Enrollment.objects.select_related('student', 'course').all()
    if course_filter:
        enrollments = enrollments.filter(course__id=course_filter)
    if status_filter:
        enrollments = enrollments.filter(status=status_filter)
    courses = Course.objects.all()
    return render(request, 'students/enrollment_list.html', {
        'enrollments': enrollments,
        'courses': courses,
        'course_filter': course_filter,
        'status_filter': status_filter,
    })


def enrollment_create(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Enrollment recorded successfully.')
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm()
    return render(request, 'students/enrollment_form.html', {'form': form})


def enrollment_delete(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == 'POST':
        enrollment.delete()
        messages.success(request, 'Enrollment removed.')
        return redirect('enrollment_list')
    return render(request, 'students/enrollment_confirm_delete.html', {'object': enrollment})
