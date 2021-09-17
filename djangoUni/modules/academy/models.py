from django.db import models
from django.db.models.base import Model

# Create your models here.

class CollegeCareer(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=50)
    time = models.PositiveBigIntegerField(default=5)

class Student(models.Model):
    DNI = models.CharField(max_length=8, primary_key=True)
    lastNames = models.CharField(max_length=70)
    name = models.CharField(max_length=35)
    dateBirth = models.DateField()
    genders = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other')
    ]
    gender = models.CharField(max_length=1, choices=genders, default='M')
    career = models.ForeignKey(CollegeCareer, null=False, blank=False, on_delete=models.CASCADE)
    validiti = models.BooleanField(default=True)

    def fullName(self):
        return '{} {}'.format(self.lastNames, self.name)

class Course(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=30)
    money = models.PositiveSmallIntegerField()
    teacher = models.CharField(max_length=100)

class Degree(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, null=False, blank=False, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=False, blank=False, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)