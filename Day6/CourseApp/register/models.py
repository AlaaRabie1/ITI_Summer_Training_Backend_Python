from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    course =  models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"Student id = {self.id}, name: {self.name}"