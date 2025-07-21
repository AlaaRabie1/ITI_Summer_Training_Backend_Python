from django import forms
from .models import Student, Course

class RegisterStudentForm(forms.Form):
    name = forms.CharField(max_length=50, label = "Full Name")
    email = forms.EmailField(label = "Email Address")
    course = forms.ModelChoiceField(queryset=Course.objects.all(), label = "Course", required=True)