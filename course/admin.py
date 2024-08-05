from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.teachers)
admin.site.register(models.CourseBack)
admin.site.register(models.CourseFront)
admin.site.register(models.CourseGraphics)


