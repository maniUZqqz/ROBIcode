import datetime
from django.db import models


class teachers(models.Model):
    name = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    telegram_id = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


class CourseBack(models.Model):
    image = models.ImageField(upload_to='upload/course/back/', null=True, blank=True)
    video_file = models.FileField(upload_to='videos/course/back', null=True, blank=True)
    title = models.CharField(max_length=100)
    short_description = models.TextField(max_length=500)
    description = models.TextField(max_length=5000)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.IntegerField()
    level = models.CharField(max_length=40)
    start_date = models.DateField()
    time_limit = models.TimeField(default=datetime.datetime.today())
    teacher = models.ForeignKey(teachers, on_delete=models.CASCADE)


class CourseFront(models.Model):
    image = models.ImageField(upload_to='upload/course/front/', null=True, blank=True)
    video_file = models.FileField(upload_to='videos/course/front/', null=True, blank=True)
    title = models.CharField(max_length=100)
    short_description = models.TextField(max_length=500)
    description = models.TextField(max_length=5000)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.IntegerField()
    level = models.CharField(max_length=40)
    start_date = models.DateField()
    time_limit = models.TimeField(default=datetime.datetime.today())
    teacher = models.ForeignKey(teachers, on_delete=models.CASCADE)

class CourseGraphics(models.Model):
    image = models.ImageField(upload_to='upload/course/graphics/', null=True, blank=True)
    video_file = models.FileField(upload_to='videos/course/graphics/', null=True, blank=True)
    title = models.CharField(max_length=100)
    short_description = models.TextField(max_length=500)
    description = models.TextField(max_length=5000)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.IntegerField()
    level = models.CharField(max_length=40)
    start_date = models.DateField()
    time_limit = models.TimeField(default=datetime.datetime.today())
    teacher = models.ForeignKey(teachers, on_delete=models.CASCADE)






