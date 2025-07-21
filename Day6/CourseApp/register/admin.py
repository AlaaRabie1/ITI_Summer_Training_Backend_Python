from django.contrib import admin
from .models import Course, Student

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'course')
    search_fields = ('name', 'email')
    list_filter = ('course',)

admin.site.register(Course, CourseAdmin)

admin.site.register(Student, StudentAdmin)