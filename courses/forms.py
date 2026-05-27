from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'name', 'description', 'units', 'instructor']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. CS101'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Introduction to Computing'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'units': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 6}),
            'instructor': forms.TextInput(attrs={'class': 'form-control'}),
        }
