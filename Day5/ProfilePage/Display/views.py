from django.shortcuts import render

# Create your views here.
def profile(request):
    name = "Alaa Rabie"
    bio = "welcome to my profile"
    skills = ["c++", "java", "python"]
    return render(request, 'Display/profile.html', {"name": name, "bio": bio, "skills": skills, "is_login": True})
