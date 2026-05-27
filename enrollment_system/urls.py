from django.contrib import admin
from django.urls import path, include
from students.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('courses/', include('courses.urls')),
    path('students/', include('students.urls')),
]
