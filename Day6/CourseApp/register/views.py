from django.shortcuts import render
from .form import RegisterStudentForm
from django.http import HttpResponse
from .models import Student, Course

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterStudentForm(request.POST)
        if form.is_valid():
            print("cleaned data:", form.cleaned_data)

            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            course = form.cleaned_data.get('course')

            if course is not None:
                Student.objects.create(
                    name=name,
                    email=email,
                    course=course
                )
                return HttpResponse("your data is valid, Thank you!")
            else:
                form.add_error('course', 'you must select a valid course')
        else:
            print("form errors:", form.errors)
    
    else:
        form = RegisterStudentForm()
        
    return render(request, 'register/registration.html',{'form': form})